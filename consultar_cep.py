import requests

cep = input('Digite o CEP ou logradouro:')

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    localidade = dic_requisicao['localidade']
    logradouro = dic_requisicao['logradouro']
    cep = '{}-{}'.format(cep[:5], cep[5:])
    print(f'{logradouro} - {bairro}, {localidade} - {uf}, {cep}')
else:
    print("CEP Inválido")