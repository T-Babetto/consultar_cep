import requests

menu = int(input('Para saber o endereço digite [1] e para saber o CEP digite [2]:'))

if menu == 1:
    cep = input('Digite o CEP:')
    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        resposta = requests.get(link)

        dic_resposta = resposta.json()

        uf = dic_resposta['uf']
        bairro = dic_resposta['bairro']
        localidade = dic_resposta['localidade']
        logradouro = dic_resposta['logradouro']
        cep = '{}-{}'.format(cep[:5], cep[5:])
        print(f'{logradouro} - {bairro}, {localidade} - {uf}, {cep}')
    else:
        print("CEP Inválido")
elif menu == 2:
    estado = str(input('Digite o UF:'))
    municipio = str(input('Digite a cidade:'))
    rua = str(input('Digite a rua:'))
    if len(rua) > 3 and len(municipio) > 3:
        link = f'https://viacep.com.br/ws/{estado}/{municipio}/{rua}/json/'

        resposta = requests.get(link)

        dic_resposta = list(resposta.json())

        for dados in dic_resposta:
            print(dados['logradouro'] + ' - ' + dados['bairro'] + ',' + dados['localidade'] + ' - ' + dados['uf'] + ', ' + dados['cep'])
    else:
        print("Endereço Inválido")

