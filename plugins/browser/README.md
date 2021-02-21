# Browser

## Certificado cliente

Comando exportar um certificado .p12 para ser utilizado pelo navegador.

```console
mkdir cert_db
certutil -N -d sql:cert_db/
pk12util -n custom-cert-name -d sql:cert_db/ -i /path/to/cert.p12
```

Referência:
https://stackoverflow.com/questions/38337976/python-selenium-how-to-specify-a-client-certificate-to-use-in-client-ssl-authe
