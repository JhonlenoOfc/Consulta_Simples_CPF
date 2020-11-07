import requests
from time import sleep


while True:
    print('')
    print("-=-"*20)
    print("BOT MASK BUSCAS")
    print('')
    opcao = int(input("O QUE DESEJA CONSULTAR ?\n1)CPF\n2)CEP\n3)CNPJ\n4)SAIR\nDIGITE O NUMERO DA OPÇÃO DESEJADA :"))
    print('')



    if opcao == 2:
        class cep:
            print('')
            cep = input('DIGITE O CEP :')
            print('CONSULTANDO, AGUARDE')
            sleep(0.5)
            print('....')
            sleep(0.5)
            print('...')
            sleep(0.5)
            print('..')
            print('')

            url = f"https://ws.apicep.com/cep/{cep}.json"
            json: object = requests.get(url).json()
            bairro = json["district"]
            estado = json["state"]
            cidade = json["city"]
            rua = json["address"]
            print('')
            print('CEP CONSULTADO COM SUCESSO!')
            print('')
            print(f'CIDADE : {cidade.upper()}\nESTADO : {estado.upper()}\nBAIRRO : {bairro.upper()}\nRUA : {rua.upper()}')
            sleep(5)
    if opcao == 1:
        class cpf:
            print('CONSULTA CPF COMPLETA')
            print('APENAS PARA CLIENTES VIPS')
            print('NUMERO PARA CONTATO 73999950864')
            print('JHON MARRA')
            print('-=-'*20)
    if opcao == 3:
        class cnpj:

            print(' ')
            cnpj = input('DIGITE O CNPJ :')
            print('CONSULTANDO, AGUARDE')
            sleep(0.5)
            print('....')
            sleep(0.5)
            print('...')
            sleep(0.5)
            print('..')
            print('')
            url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
            cpj = requests.get(url).json()
            nome = cpj["nome"]
            nome_fantasia = cpj["fantasia"]
            estado = cpj["uf"]
            telefone = cpj["telefone"]
            email = cpj["email"]
            data_abertura = cpj["abertura"]
            capital = cpj["capital_social"]
            situacao = cpj["situacao"]
            municipio = cpj["municipio"]
            bairro = cpj["bairro"]
            rua = cpj["logradouro"]
            cep = cpj["cep"]
            porte = cpj["porte"]
            atvd = cpj["atividade_principal"]
            print('')
            print('CNPJ CONSULTADO COM SUCESSO')
            print('')
            print(f'ATIVIDADE : {atvd}NOME : {nome}\nNOME FANTASIA : {nome_fantasia}\nESTADO : {estado}\nTELEFONE : {telefone}\nEMAIL : {email}\nDATA DE ABERTURA : {data_abertura}\nPORTE : {porte}\nCAPITAL SOCIAL : {capital}\nSITUAÇÃO : {situacao}\nMUNICIPIO : {municipio}\nBAIRRO : {bairro}\nRUA : {rua}\nCEP : {cep}')
            print('')
            sleep(5)
    else:
        print('')
        print("Tchau corno!")
        break
