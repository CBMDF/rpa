# Browser

## Certificado cliente - Firefox

Comando exportar um certificado .p12 para ser utilizado pelo navegador.

```console
mkdir cert_db
certutil -N -d sql:cert_db/
pk12util -n custom-cert-name -d sql:cert_db/ -i /path/to/cert.p12
```

Referência:
 - https://stackoverflow.com/questions/38337976/python-selenium-how-to-specify-a-client-certificate-to-use-in-client-ssl-authe

## Seleção automática de certificado - Chrome

### Chave de Registro no Windows

Chave:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls
```
Valor:

```
 {"pattern":"*","filter":{}}"
```

### Arquivo JSON de política no Linux

Criar o arquivo `auto_select_certificate.json` com o seguinte conteúdo

```json
{
  "AutoSelectCertificateForUrls": [ "{\"pattern\":\"*\",\"filter\":{}}" ]
}
```
Então copiá-lo para os diretórios conforme abaixo:

```
$HOME/etc/opt/chrome/policies/managed/auto_select_certificate.json
$HOME/etc/opt/auto_select_certificate.json
```

Referência:
 - http://www.chromium.org/administrators/policy-list-3#AutoSelectCertificateForUrls
 - https://github.com/sgedda/Selenium.Docker.Certficate
