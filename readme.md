# Generación de Certificados (on demand)

## Problema:
Diariamente recibe solicitudes del equipo comercial externo para generar un certificado de estado de contrato y saldo promedio de comisiones. Actualmente se genera de forma manual este certificado, se busca un proceso más automático.

## Propuesta de solución:
Disponer una web para solicitud y descarga del certificado, bajo el siguiente esquema:
 ![image](https://github.com/user-attachments/assets/7c79b2d9-d417-49af-b6ba-85f3c9fdfbb3)


### Detalle del flujo del proceso:

![image](https://github.com/user-attachments/assets/963165a0-13f6-469a-87a6-7a6ff03e2728)

 
## Implementación:
1.	Crear el esquema y la tabla en bigquery
2.	Crear el bucket
3.	Deploy en cloud run con los objetos del proyecto

## Mock-up 

![image](https://github.com/user-attachments/assets/86203526-0d4a-4bcd-8d4d-cb52c93df1b5)

![image](https://github.com/user-attachments/assets/aaacc577-9bb3-4b3f-bdc0-ab7c61167cbf)

![image](https://github.com/user-attachments/assets/03cd04e1-4740-495e-a362-16f6cbb07d6a)

![image](https://github.com/user-attachments/assets/c728013e-45c6-4fc1-a011-149cc09c15f4)

![image](https://github.com/user-attachments/assets/d9dc34e2-9c94-4763-8b90-0974c685508e)


## Evolutivos:
1 	Implementar un key.json para que el entorno de CGS no sea público

2 	Ubicar la funcionalidad dentro de un portal de funcionalidades

3 	Ingestar actualizaciones de los datos a bigquery de forma mensual, garantizando un promedio de comisiones real y actualizado.
