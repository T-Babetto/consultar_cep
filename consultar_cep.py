import requests

cep = input('Digite o CEP ou logradouro:')

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(link)

    dic_resposta = resposta.json()

    uf = dic_resposta['uf']
    cidade = dic_resposta['localidade']
    bairro = dic_resposta['bairro']
    localidade = dic_resposta['localidade']
    logradouro = dic_resposta['logradouro']
    cep = '{}-{}'.format(cep[:5], cep[5:])
    print(f'{logradouro} - {bairro}, {localidade} - {uf}, {cep}')
else:
    print("CEP Inválido")