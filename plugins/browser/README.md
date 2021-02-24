# Browser

## Importando certificado cliente .p12 para o Trust Database Files cert8.db

Comando exportar um certificado .p12 para ser utilizado pelo navegador.

```console
mkdir cert_db
certutil -N -d sql:cert_db/
pk12util -n custom-cert-name -d sql:cert_db/ -i /path/to/cert.p12
```

Referência:

- <https://stackoverflow.com/questions/38337976/python-selenium-how-to-specify-a-client-certificate-to-use-in-client-ssl-authe>
- <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/tools/NSS_Tools_certutil>
- <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/tools/NSS_Tools_pk12util>

## Seleção automática de certificado - Chrome

### Chave de Registro no Windows

No Windows, para que o Chrome selecione automaticamente o Certificado Cliente, adicione a seguinte chave no registro:
`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls`

com o valor `{"pattern":"*","filter":{}}`

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls]
"1"="{\"pattern\": \"*\", \"filter\": {} }"
```

Referência:
 - https://cloud.google.com/docs/chrome-enterprise/policies/?policy=AutoSelectCertificateForUrls

Para verificar se a política foi aplicada corretamente, abra no Chrome a seguinte URL: `chrome://policy/`

### Arquivo JSON de política no Linux

Criar o arquivo `auto_select_certificate.json` com o seguinte conteúdo

```json
{
  "AutoSelectCertificateForUrls": ["{\"pattern\":\"*\",\"filter\":{}}"]
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
