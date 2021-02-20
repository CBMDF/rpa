from plugins.exchange2016 import exchange2016
import yaml


class RPA:

    def __init__(self) -> None:
        with open("examples/download-anexo-email.yaml") as file:
            cfg = yaml.load(file, Loader=yaml.BaseLoader)
            print(cfg['jobs']['download-email']
                  ['steps'][0]['with']['username'])


RPA()
