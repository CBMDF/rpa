#   RPA - Dados públicos CNPJ

Realiza o download e descompacta os arquivos zip da base de dados públicos CNPJ.

## Instalação

Abra o terminal no diretório base-cnpj e digite os seguintes comandos:

```console
pip install virtualenv
```

```console
virtualenv env
```

Ative o ambiente virtual e instale as dependências

```console
env\Scripts\activate
(env) pip install -r requirements.txt
```

Para rodar o script
```console
python base_cnpj.py
```

## Agendador de Tarefas

Ao criar uma nova tarefa no Agendador de Tarefas preencha os campos da aba ações conforme indicado abaixo:

![alt text](https://i.imgur.com/iValV12.png)

<b>- Programa/Script:</b> Endereço do executável pythonw.exe, encontrado dentro da pasta Scripts do ambiente virtual. <br/>
<b>- Adicione argumentos:</b> Nome do script python. <br/>
<b>- Iniciar em:</b> Endereço do diretório base-cnpj. <br/>



# ETL - Dados públicos CNPJ

Para a importação desses dados de CNPJ é utilizado o Pentaho, que subirá os arquivos para o banco de dados Postgresql. Para utilizar o Pentaho é necessário a instalação do Java jdk-8, e para a administração do Postgresql é preciso do pgAdmin4.


## Java jdk-8

#### Instalação 

Para a instalação, tanto no Linux quanto no Windows, basta acessar o link abaixo:
https://www.oracle.com/br/java/technologies/javase/javase-jdk8-downloads.html

## Postgresql

#### Instalação 

Para a instalação no Windows basta acessar o link abaixo:
https://www.postgresql.org/download/

Quando finalizar o download, vamos abrir o arquivo de instalação. Você vai precisar: selecionar a basta onde vai ser instalado; escolher quais recursos instalar junto com o Postgresql (pode deixar todos marcados); escolher a pasta onde os dados do Postgres serão salvos; definir a senha de acesso do usuário; definir a porta que o Postgres irá rodar; escolher o idioma; depois vão aparecer mais 3 janelas que é só apertar em Next, Next e Finish.

Para a instalação no Linux:

Por padrão, o repositório do Ubuntu vem com o PostgreSQL disponível, bastando acionar o comando apt-get no terminal, digitando as seguintes linhas:

```console
#sudo apt update
```
```console
#sudo apt install postgresql postgresql-contrib
```
#### Configuração

Depois de instalado o Postgres você vai procurar pelo programa pgAdmin4, que é uma plataforma para administrar o Postgres. Ele vai pedir a senha que você definiu na instalação e aí você vai começar a configurar criando um servidor, um banco, um schema e a partir daí começar a criar as tabelas e colunas baseadas no layout e no arquivo de base de dados de CNPJ.

## Pentaho

#### Instalação 

Para a instalação, tanto no Linux quanto no Windows, basta acessar o link abaixo:
https://sourceforge.net/projects/pentaho/

#### Configuração

Depois de instalado, vai ser criado uma pasta com o nome "pdi-ce", você vai abrir até chegar na pasta "data-integration". O arquivo executável para abrir no Windows é o "Spoon.bat". Já no Linux, você vai precisar abrir essa pasta (data-integration) no terminal e digitar "./spoon.sh".

Vai ser preciso criar uma transformação para cada arquivo. Assim que você abre uma transformação o Pentaho te dá diversas opções de design, nesse caso vai ser preciso somente do Input que será a opção CSV file Input e do Output que será Table Output. Abrindo o CSV file Input você vai selecionar o arquivo .CSV, informar qual o delimitador e a forma de enclausuramento de dados usado no arquivo, desmarcar a opção de Header row e obter os campos. Depois de obitido, o próprio Pentaho dá nomes as colunas e coloca o tipo de dado, mas precisa alterar e colocar igual foi colocado no pgAdmin e apagar as outras informações que ele mesmo adicionou. Clicando nesse ícone do CSV file aparece algumas opções, clica na cria um conector output e liga no Table Output.

Abrindo agora o Table Output na opção Geral é preciso colocar o nome da conexão, o tipo, nome do servidor, do banco, usuário e senha definidos no pgAdmin e marcar a terceira opção na opções avançadas. Depois disso é preciso escolher o nome do schema e da tabela para qual vão os dados, marcar a opção de especificar os campos do banco de dados para conferir o nome das colunas.

É só executar a transformação e fazer a mesma coisa com todos os arquivos.

Para facilitar e deixar mais automatizado, tem a opção de criar um Job para cada tipo de CNPJ para não ficar tão pesado em 1 arquivo só (empresa, estabelecimento e socio). Vai ser precisar de um Start, 10 transformações e um Sucess, conectar todos esses arquivos com um conector output e dentro das transformações selecionar o arquivo .ktr e executar o Job.
