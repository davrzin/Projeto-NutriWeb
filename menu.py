import getpass as gp

def menu(): #Abre o menu
    print("O que você deseja fazer:\n"
          "1 - Login\n"
          "2 - Cadastrar Usuário\n"
          "0 - Sair")
    op = int(input("Digite uma Opção: "))
    if 0 <= op <= 2:
        return op
    else:
        print("Opção Inválida")

def carregar_usuarios(): #Carrega os dados do usuários
    usuarios_dict = {}

    try:
        with open("usuarios.txt", "r") as arquivo:
            conteudo = arquivo.read()
            usuarios = conteudo.split('\n\n')

            for usuario in usuarios:
                usuario_info = {}
                linhas = usuario.split('\n')

                for linha in linhas:
                    if ':' in linha:
                        chave, valor = linha.split(': ')
                        usuario_info[chave] = valor

                if "Email" in usuario_info:
                    email = usuario_info["Email"]
                    usuarios_dict[email] = usuario_info

    except FileNotFoundError:
        pass

    return usuarios_dict

def cadastro():#Cadastra o Usuário
    usuarios = carregar_usuarios()

    email = input("Digite um email: ")
    senha = gp.getpass("Crie uma Senha: ")
    nome = input("Digite seu Nome: ")
    sexo = input("Digite seu Sexo: ")
    idade = int(input("Digite sua Idade: "))
    peso = float(input("Digite seu Peso: "))
    altura = float(input("Digite sua Altura: "))
    objetivo = input("Digite seu Objetivo: ")

    if email in usuarios:
        print("Email já cadastrado.")
    else:
        with open("usuarios.txt", "a") as arquivo:
            usuario = f"Email: {email}\nSenha: {senha}\nNome: {nome}\nSexo: {sexo}\nIdade: {idade}\nPeso: {peso}\nAltura: {altura}\nObjetivo: {objetivo}\n\n"
            arquivo.write(usuario)
            print("Cadastro Efetuado!")

def login(): #Faz o Login
    usuarios = carregar_usuarios()

    email = input("Digite seu e-mail: ")
    senha = gp.getpass("Digite sua senha: ")

    if email in usuarios:
        usuario = usuarios[email]
        if usuario["Senha"] == senha:
            print("Login Efetuado!")
            print("Dados do usuário:")
            for chave, valor in usuario.items():
                print(f"{chave}: {valor}")
        else:
            print("Senha incorreta.")
    else:
        print("Email não encontrado.")

def EscolhaMenu():#Excução do programa
    escolha = menu()

    if(escolha == 1):
        login()

    elif(escolha == 2):
        cadastro()

    else:
        print("tchau")

try:
    with open("usuarios.txt", "r") as arquivo:
        pass
except FileNotFoundError:
    with open("usuarios.txt", "w") as arquivo:
        pass

EscolhaMenu()
