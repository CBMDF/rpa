from plugins import Plugin
import xmltodict


class nfexml(Plugin):

    def __init__(self):
        super().__init__()

    def extrair(self, filePath):

        with open(filePath, "rb") as arquivo:

            doc = xmltodict.parse(arquivo, xml_attribs=True)
            valorNota = doc["nfeProc"]["NFe"]["infNFe"]["pag"]["detPag"]["vPag"]
            CNPJEmitente = doc["nfeProc"]["NFe"]["infNFe"]["emit"]["CNPJ"]
            NomeEmitente = doc["nfeProc"]["NFe"]["infNFe"]["emit"]["xNome"]
            FantasiaEmitente = doc["nfeProc"]["NFe"]["infNFe"]["emit"]["xFant"]

            print(valorNota)
            print(CNPJEmitente)
            print(NomeEmitente)
            print(FantasiaEmitente)
