from models.jogo import Jogo
from services.jogo_service import adicionar_jogo, salvar_jogo

jogos = adicionar_jogo()

print("===============================")
print("=======SISTEMA DE JOGOS========")
print("===============================")

print("Categoria padrão: ", Jogo.catergotia_padrao())

while True:
    print("\nMENU")
    print("1- Adicionar Jogo")
    print("2- Listar Jogos")
    print("3- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nAdicionar Jogo")

        nome = input("Nome: ")
        genero = input("Genero: ")
        ano = input("Ano: ")

        novo_jogo = Jogo(nome, genero, ano)  
        jogos.append(novo_jogo)  
        salvar_jogo(jogos)  
        print("Jogo Cadastrado!")

    elif opcao == "2":
        print("\nLista de Jogos")
        if len(jogos) == 0:
            print("Nenhum jogo cadastrado")
        else:
            for i, jogo in enumerate(jogos):
                print(f"Jogo {i + 1}:")
                jogo.exibir() 

    elif opcao == "3":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")