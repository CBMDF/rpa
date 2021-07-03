# RPA - Dados públicos CNPJ

Realiza por meio do Python o download e descompactação dos arquivos zip da base de dados públicos CNPJ, em seguida, com o uso do Pentaho é realizado a carga dos arquivos com formato CSV obtidos na descompactação para um bando de dados PostgreSQL.

## Pré-requisitos
É necessário que tenha instalado em sua máquina o [Python](https://www.python.org/downloads/) 3 ou superior, [PostgreSQL](https://www.postgresql.org/download/) e a ferramenta [Pentaho](https://sourceforge.net/projects/pentaho/). Para o funcionamento do pentaho é necessário que tenha o [Java SE Development Kit](https://www.oracle.com/br/java/technologies/javase/javase-jdk8-downloads.html) instalado em sua máquina.

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
