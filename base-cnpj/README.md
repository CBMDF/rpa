# RPA - Dados públicos CNPJ

Realiza por meio do Python o download e descompactação dos arquivos zip da base de dados públicos CNPJ, em seguida, com o uso do Pentaho é realizado a carga dos arquivos com formato CSV obtidos na descompactação para um bando de dados PostgreSQL.

## Pré-requisitos

### Java JDK-8

Para a instalação, tanto no Linux quanto no Windows, basta acessar o link abaixo:
<https://www.oracle.com/br/java/technologies/javase/javase-jdk8-downloads.html>

### Postgresql

Para a instalação no Windows basta acessar o link abaixo:
<https://www.postgresql.org/download/>

Quando finalizar o download, vamos abrir o arquivo de instalação. Você vai precisar: selecionar a basta onde vai ser instalado; escolher quais recursos instalar junto com o Postgresql (pode deixar todos marcados); escolher a pasta onde os dados do Postgres serão salvos; definir a senha de acesso do usuário; definir a porta que o Postgres irá rodar; escolher o idioma; depois vão aparecer mais 3 janelas que é só apertar em Next, Next e Finish.

Para a instalação no Linux:
Por padrão, o repositório do Ubuntu vem com o PostgreSQL disponível, bastando acionar o comando apt-get no terminal, digitando as seguintes linhas:
```console
#sudo apt update
```
```console
#sudo apt install postgresql postgresql-contrib
```

### Pentaho

Para a instalação, tanto no Linux quanto no Windows, basta acessar o link abaixo:
https://sourceforge.net/projects/pentaho/

Depois de instalado, vai ser criado uma pasta com o nome "pdi-ce", você vai abrir até chegar na pasta "data-integration". O arquivo executável para abrir no Windows é o "Spoon.bat". Já no Linux, você vai precisar abrir essa pasta (data-integration) no terminal e digitar "./spoon.sh".

## ETL - Configurações

### Inicializador Pentaho
Configure o arquivo **init_pdi.bat** localizado na pasta ETL, especificando o endereço da ferramenta de linha de comando **Kitchen.bat**:
```
SET kitchen=<caminho_do_arquivo>\Kitchen.bat
```

### Banco de dados
Crie um Schema com nome "cnpj" em seu banco de dados e configure o arquivo **config.json** localizado na pasta ETL, especificando as credenciais do banco de dados:
```
[
    {
      "hostname": "<hostname>",
      "database": "<database>",
      "port": "<port>",
      "username": "<username>",
      "password": "<password>"
    }
]
```

Para verificar o correto funcionamento do processo de ETL execute o **init_pdi.bat**, será realizado a carga de arquivos CSV com tamanhos reduzidos especificamente para esse teste. Caso ocorra erros durante o processo, verifique o arquivo **log.txt** gerado.

## Start
O arquivo **start.bat** inicializa todo processo de download e carga dos arquivos de Dados publicos CNPJ.
