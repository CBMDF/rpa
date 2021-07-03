# RPA - Dados públicos CNPJ

Realiza por meio do Python o download e descompactação dos arquivos zip da base de dados públicos CNPJ, em seguida, com o uso do Pentaho é realizado a carga dos arquivos com formato .csv obtidos na descompactação para um bando de dados PostgreSQL.

## Pré-requisitos
É necessário que tenha instalado em sua máquina o [Python](https://www.python.org/downloads/) 3 ou superior, [PostgreSQL](https://www.postgresql.org/download/,) e a ferramenta [Pentaho](https://sourceforge.net/projects/pentaho/). Para o funcionamento do pentaho é necessário que tenha instalado em sua máquina o [JDK](https://www.oracle.com/br/java/technologies/javase-jdk11-downloads.html), preferencialmente em sua versão mais recente.

## ETL - Configurações

### Inicializador Pentaho
Configure o arquivo **init_pdi.bat** localizado na pasta ETL, especificando o endereço do **Kitchen.bat**:
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

Para verificar o correto funcionamento do processo de ETL execute o **init_pdi.bat**, será gerado um log.txt com todo processo 
de carga dos arquivos no formato .csv reduzidos especificamente para esse teste. Verifique o conteúdo do log.txt para descartar
a existência de erros durante o processo.

## Start
O arquivo **start.bat** inicializa todo processo de download e carga dos arquivos de Dados publicos CNPJ.
