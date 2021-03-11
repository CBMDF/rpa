# Expresso

Plugin de integração com a interface web do [Expresso Livre](http://www.expressolivre.org).

## Exemplo

```python
from plugins.expresso import Expresso
import time

ex = Expresso()

ex.login('https://webmail.cbm.df.gov.br', 'ada', 'lovelace')

search_query = {"from": 'usuario@exemplo.df.gov.br',
                "to": '', "body": '',
                "subject": 'Planilha 2021',
                "start_date": '', "end_date": '',
                "on_date": '28012021'}
ex.search_message(search_query=search_query)
time.sleep(10)
ex.logout()
```
