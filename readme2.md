# General GCP Commands Cheat Sheet

## Set Account
When having more than one account, this command helps switching between them.

```bash
gcloud config set account "your-email@example.com"
```

You can check the changes with:

```
gcloud auth list
```

Also, before setting the project, it may ask you to login:

```
gcloud auth login
```
