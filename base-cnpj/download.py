'''
Este script realiza o download e descompacta os arquivos zip da base de dados públicos
CNPJ e verifica a necessidade de uma atualização dessa base de dados.
'''

import requests
import zipfile
import shutil
import sys
import os
import traceback
import tqdm
import signal
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def download(url, directory):
    '''
    Realiza o download de um arquivo. Retorna um boolean = 'True' caso o download seja bem sucedido.

    url: Url do download.
    directory: Diretório em que o arquivo será salvo.
    '''

    try:
        response = requests.get(url, stream=True)
        full_url = urlparse(url)
        file_name = os.path.basename(full_url.path)
        file_size = int(response.headers['Content-Length'], 0)
        chunk = 1
        chunk_size = 1024
        num_bars = int(file_size / chunk_size)
        address = os.path.join(directory, file_name)

        with open(address, 'wb') as new_file:

            try:

                for chunk in tqdm.tqdm(
                    # progressbar stays
                    response.iter_content(chunk_size=chunk_size), total=num_bars, unit='KB', desc=file_name, leave=True
                ):

                    new_file.write(chunk)

            except KeyboardInterrupt:
                print(
                    "Deseja realmente encerrar o processo de download? [s/N]")
                choice = input().lower()
                if choice == 's':
                    exit(1)
                else:
                    pass

        return True

    except Exception as e:
        print(traceback.format_exc())
        return False

def extract(directory, file_name):
    '''
    Descompacta um arquivo zip. Retorna um boolean = 'True' caso obtenha sucesso

    directory: Diretório do arquivo
    file_name: Nome do arquivo 
    '''

    file_address = os.path.join(directory, file_name)

    try:
        with zipfile.ZipFile(file_address, 'r') as zip_ref:
            zip_ref.extractall(directory)
    except Exception as e:
        print(traceback.format_exc())
        return False
    else:
        try:
            os.remove(file_address)
        except:
            print('Ocorreu um erro ao excluir o arquivo {}'.format(file_name))
            return False
        
        return True

def get_urls(elements):
    '''
    Obtém as urls que estão inseridas em uma lista de classes. Retorna uma lista de urls

    elements: Lista de classes
    '''
    urls = []
    urls.append(elements_found[36].get('href'))

    for i in range(30):
        urls.append(elements_found[i].get('href'))

    return urls

def delete_all_files(directory):
    
    files = os.listdir(directory)

    for file in files:

        address = os.path.join(directory, file)

        try:
            os.remove(address)
        except:
            print('Ocorreu um erro ao excluir o arquivo {}'.format(files))
            return False

    return True

def check_update(urls, directory):

    files = os.listdir(directory)
    control = 0

    for url in urls:

        full_url = urlparse(url)
        file_name = os.path.basename(full_url.path)
        csv_file_name = file_name[:-4]

        if csv_file_name in files:
            control += 1

    if control == len(files):
        return False
    else:
        return True

url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'

response = requests.get(url)

if response.status_code != requests.codes.OK:
    print('Ocorreu um erro ao acessar {}'.format(url))
    sys.exit(1)

response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

elements_found = soup.find_all(class_='external-link')

urls = get_urls(elements_found)  # Chamada da função get_urls

# Download e extração dos arquivos zip
directory = 'ETL/csv-files'

status = check_update(urls, directory) # Verificar necessidade da atualização
if status == False:
    print('A base de dados públicos CNPJ já está atualizada.')
    sys.exit(0)
else:
    delete_all_files(directory) # Deletar arquivos do diretório

for url in urls:
    full_url = urlparse(url)
    file_name = os.path.basename(full_url.path)
    
    status = download(url, directory) # Chamada função 'download'
    if status == False:
        break

    status = extract(directory, file_name) # Chamada função 'extract'
    if status == False:
        break

if status == True:
    print('Download e extração dos arquivos concluída com sucesso')
    sys.exit(0)
else:
    sys.exit(1)
