from flask import Flask, request, render_template, jsonify
from google.cloud import bigquery, storage
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("index.html")

@app.route("/generar", methods=["POST"])
def generar_certificado():
    data = request.get_json()
    nombre = data.get("nombre")
    documento = data.get("documento")
    tipo = data.get("tipo_certificado")

    if not nombre or not documento or not tipo:
        return jsonify({"error": "Faltan campos"}), 400

    client_bq = bigquery.Client()
    query = """
        SELECT nombre, estado, saldo FROM `hazel-design-463214-v7.proyectofinal.afiliados`
        WHERE documento = @documento LIMIT 1
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("documento", "STRING", documento)]
    )
    result = client_bq.query(query, job_config=job_config).result()
    row = next(iter(result), None)
    if not row or row.estado != "activo":
        return jsonify({"error": "No autorizado"}), 403

    # Crear PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, f"Certificamos que {row.nombre} está afiliado.")
    if tipo == "saldo":
        pdf.drawString(100, 690, f"Saldo disponible: ${row.saldo:,.2f}")
    else:
        pdf.drawString(100, 690, "Este certificado no incluye información de saldo.")
    pdf.drawString(100, 710, f"Fecha: {datetime.utcnow().date()}")
    pdf.save()
    buffer.seek(0)

    # Subir a Cloud Storage
    filename = f"{documento}_{int(datetime.utcnow().timestamp())}.pdf"
    bucket_name = "certificados-temporales-lv"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_file(buffer, content_type="application/pdf")    
    url = f"https://storage.googleapis.com/{bucket_name}/{filename}"
    return jsonify({"url_certificado": url})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
