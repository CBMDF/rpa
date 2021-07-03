# RPA - Dados públicos CNPJ

Realiza por meio do Python o download e descompactação dos arquivos zip da base de dados públicos CNPJ, em seguida, realiza a carga dos arquivos csv obtidos na descompactação para um bando de dados PostgreSQL, para realizar esse processo é utilizado a ferramenta pentaho.

## Pré-requisitos
Será necessário que tenha instalado em sua máquina o [Python](https://www.python.org/downloads/) 3 ou superior, [PostgreSQL](https://www.postgresql.org/download/,) e a ferramenta [Pentaho](https://sourceforge.net/projects/pentaho/). Para o funcionamento do pentaho é necessário que tenha instalado em sua máquina o [JDK](https://www.oracle.com/br/java/technologies/javase-jdk11-downloads.html), preferencialmente em sua versão mais recente.

## ETL - Configurações

### Inicializador Pentaho
Configure o **init_pdi.bat** localizado na pasta ETL, especificando o endereço do Kitchen.bat:
```
SET kitchen=C:\pentaho\data-integration\Kitchen.bat
```

### Banco de dados
Configure o arquivo **config.json** localizado na pasta ETL, especificando as credenciais do banco de dados:
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

## Instalação do Postgresql

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

### Configuração do PostgreSQL

Depois de instalado o Postgres você vai procurar pelo programa pgAdmin4, que é uma plataforma para administrar o Postgres. Ele vai pedir a senha que você definiu na instalação e aí você vai começar a configurar criando um servidor, um banco, um schema e a partir daí começar a criar as tabelas e colunas baseadas no layout e no arquivo de base de dados de CNPJ.

## Instalação do Pentaho

Para a instalação, tanto no Linux quanto no Windows, basta acessar o link abaixo:
https://sourceforge.net/projects/pentaho/

Depois de instalado, vai ser criada uma pasta denominada "pdi-ce-9.1.0.0-324", abrindo a pasta "data-integration" terá o arquivo executável que no Windows é o "Spoon.bat". Já no Linux, é preciso abrir essa pasta (data-integration) no terminal e digitar:

```console
# ./spoon.sh
```

### Configuração do Pentaho

