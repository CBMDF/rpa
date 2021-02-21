# CBMDF RPA

Robotic process automation

Utiliza um arquivo yaml inspirado no GitHub actions para configurar as ações automáticas que serão executadas.

## Instalação

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

## Exemplo com código Python

```python
from plugins.browser import Browser

url = 'https://www.learningcontainer.com/sample-zip-files/'
browser = Browser()
browser.openUrl(url=url)
browser.click("//html/body/div[1]/div/div[1]/main/article/div/div[2]/p[5]/a")
```

## Plugins

```yaml
---
# (Obrigatório) Nome do robô
name: Apenas login no e-mail

# (Opcional) Se não for especificado o robô deverá ser executado manualmente.
on:
  schedule:
    # 2022-01-01 00:00:00
    - cron: "0 0 1 1 *"

# Tarefas que serão realizadas pelo robô utilizando os plugins suportados
jobs:
  download-email: # Nome da tarefa.
    steps:
      - name: Login
        uses: plugins/exchange2016
        with:
          url: https://cas.exemplo.com.br/owa/
          username: ${{ secrets.USERNAME }}
          password: ${{ secrets.PASSWORD }}
      - name: Pesquisar Mensagem
        with:
```

### Microsoft Exchange Server 2016

### AgenciaNet

### Comando de Terminal
