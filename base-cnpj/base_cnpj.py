'''
Este script realiza o download e extração dos arquivos da base de dados públicos
CNPJ e verifica a necessidade da atualização dessa base de dados.
'''

import requests, zipfile, shutil, sys, os
from bs4 import BeautifulSoup

def download_file(url, address):
    '''
    Realiza o download de um arquivo. Retorna um boolean = 'True' caso o download seja bem sucedido.

    url: Url do download.
    address: Diretório em que o arquivo baixado será salvo.
    '''
    try:
        response = requests.get(url, stream=True)

        with open(address, 'wb') as new_file:
            for chunk in response.iter_content(chunk_size=1024):
                new_file.write(chunk)
    except:
        status = False
    else:
        status = True

    return status

def extract_files(file_address, final_directory):
    '''
    Realiza a extração de um arquivo zip. Retorna um boolean = 'True' caso obtenha sucesso

    file_address: Endereço do arquivo zip que será extraído
    final_directory: Diretório para qual o arquivo será extraído
    '''
    try:
        with zipfile.ZipFile(file_address, 'r') as zip_ref:
                zip_ref.extractall(final_directory)
    except:
        status = False
    else:
        status = True

    return status

def extract_urls(elements):
    '''
    Obtém as urls que estão inseridas em uma lista de classes. Retorna uma lista de urls

    elements: Lista de classes
    '''
    urls = []
    for i in range(30):
        urls.append(elements_found[i].get('href'))

    return urls

def extract_zip_files_name(urls):
    '''
    Obtém os nomes dos arquivos zip contidos nas urls. Retorna uma lista com nomes dos arquivos zip

    urls: Lista de urls
    '''
    zip_files_name = []
    for url in urls:
        zip_files_name.append(url.split("/")[-1])

    return zip_files_name

def extract_csv_files_name(zip_files_name):
    '''
    Obtém os nomes dos arquivos csv a partir de uma lista de nomes de arquivos zip. Retorna uma lista
    com os nomes dos arquivos csv.

    zip_files_name: Lista de nomes de arquivos zip
    '''
    csv_files_name = []
    for zip_file_name in zip_files_name:
        csv_files_name.append(zip_file_name[:-4])

    return csv_files_name

def check_update(csv_files_name, ouput_dir):
    '''
    Percorre cada arquivo do diretório 'output_dir' e verifica se o arquivo existe dentro da lista 'csv_files_name'.
    Retorna um boolean = 'False' se todos os arquivos pertecerem a lista e o número de arquivos ser igual ao tamanho da lista.
    Caso contrário Retorna um boolean = 'True' indicando a necessidade de uma atualização.
    
    csv_files_name: Lista de nomes dos arquivos csv.
    output_dir: Diretório onde será verificado a necessidade da atualização.
    '''
    control = 0
    for csv_file_name in csv_files_name:

        if csv_file_name in os.listdir(output_dir):
            control += 1

    if control == len(csv_files_name):
        status = False
    else:
        status = True

    return status

def move_files(files_name, directory, final_directory):
    '''
    Move de um diretório para outro, todos os arquivos cujo nome pertence a uma determinada
    lista de nomes. Retorna um boolean = 'True' caso obtenha sucesso.

    files_name: Lista de nomes dos arquivos que serão movidos.
    directory: Diretório inicial dos arquivos.
    final_directory: Diretório final dos arquivos.
    '''

    for file_name in files_name:
        address = os.path.join(directory, file_name)

        try:
            shutil.move(address, final_directory)
        except:
            status = False
            print('Ocorreu um erro ao mover o arquivo {} para {}'.format(file_name, final_directory))
            break
        else:
            status = True

    return status

def delete_files(directory, files_name):
    '''
    Deleta todos os arquivos de uma diretório com a exceção dos arquivos com nomes pertecentes a uma
    determinada lista de nomes. Retorna um boolean = 'True' caso obtenha sucesso.

    directory: Diretório do qual será excluído os arquivos.
    files_name: Lista de nomes dos arquivos que não devem ser deletados.
    '''
    
    directory_files = os.listdir(directory)

    for directory_file in directory_files:
        address = os.path.join(directory, directory_file)

        if not directory_file in files_name:
            try:
                os.remove(address)
            except:
                status = False
                print('Ocorreu um erro ao excluir o arquivo {}'.format(directory_file))
                break

        status = True

    return status

url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'

response = requests.get(url)

if response.status_code != requests.codes.OK:
    print('Ocorreu um erro ao acessar {}'.format(url))
    sys.exit()

response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

elements_found = soup.find_all(class_='external-link')


urls = extract_urls(elements_found) # Chamada da função extract_urls

zip_files_name = extract_zip_files_name(urls) # Chamada da função extract_zip_files

csv_files_name = extract_csv_files_name(zip_files_name) # Chamada da função extract_csv_files_name

# Criar diretório 'files_dir'
files_dir = 'files' # Diretório para arquivos zip

if files_dir in os.listdir():
    shutil.rmtree(files_dir)
    os.mkdir(files_dir)
else:
    os.mkdir(files_dir)

# Criar diretório 'output_dir' 
output_dir = 'output' # Diretório final

if not output_dir in os.listdir():
    os.mkdir(output_dir)


# Verificar necessidade da atualização
status = check_update(csv_files_name, output_dir)

if status == False:
    print('A base de dados públicos CNPJ já está atualizada.')
    sys.exit()

# Download arquivos zip
for i in range(len(urls)):
    
    address = os.path.join(files_dir, zip_files_name[i])
    status = download_file(urls[i], address) # Chamada da função download_file

    if status == True:
        print('Download {} concluído com êxito. ({} de {})'.format(zip_files_name[i], i+1, len(urls)))
    elif status == False:
        print('Ocorreu um erro com download do arquivo {}'.format(zip_files_name[i]))
        shutil.rmtree(files_dir)
        sys.exit()

# Extrair arquivos
for i in range(len(zip_files_name)):

    address = os.path.join(files_dir, zip_files_name[i])
    status = extract_files(address, files_dir) # Chamada da função extract_files

    if status == True:
        print('{} extraído com êxito.({} de {})'.format(zip_files_name[i], i+1, len(zip_files_name)))
        os.remove(address) # Excluir arquivo zip já extraído
    elif status == False:
        print('Ocorreu um erro ao extrair o arquivo {}.'.format(zip_files_name[i]))
        shutil.rmtree(files_dir) # Remover todo diretório 'files_dir' em caso de erro na extração de um arquivo
        sys.exit()


# Mover arquivos csv para diretório 'ouput_dir'
status = move_files(csv_files_name, files_dir, output_dir)

if status == True:
    shutil.rmtree(files_dir)
elif status == False:
    sys.exit()


# Excluir arquivos que estavam em 'ouput_dir'
status = delete_files(output_dir, csv_files_name)

if status == True:
    print('Operação realizada com sucesso.')
elif status == False:
    sys.exit()
