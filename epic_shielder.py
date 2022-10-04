#nome = '\\CAPSV\\Users\\Public\\01 - ASPER\\ACA\\12 - 0359-22 - RENAULT-MASTER ACA V20P\\PROCESSO ESCANEADO\\ENVIO ITL VIV'
import subprocess

class userCreator:
    def __init__(self):
        with open('UserList.txt', 'a') as usuarios:
            while True:
                nome = input("Digite o ID do usuario que você quer criar: ")
                if len(nome) < 6:
                    print("O tamanho do ID TEM que ter no minimo 6 caracteres!")
                else:
                    break
            
            while True:
                senha = input("Digite a senha para o Usuario que você: ")
                if len(senha) < 8:
                    print("O tamanho da senha TEM que ter no minimo 8 caracteres!")
                else:
                    break
            
            usuarios.write(nome)
            usuarios.write(senha)

class userDelete:
    with open('UserList.txt', 'w') as usuarios:
        usuarios.write('')

#class Identificacao:
#    def __init__(self):
#        usuario = input("Digite o seu ID: ")
#        senha = int(input("Digite sua senha: "))
#
#        if (usuario in usuarios.values()) and (senha in senhas.values(usuarios.keys())):
#            print("Logado")
#
#        else:
#            print("Login ou Senha INCORRETO!")

class Pasta:
    def __init__(self):

        caminho = input("Usuario digite o caminho: ")
        print(caminho)

pessoa1 = userCreator()

#Pasta()