import json
from models.jogo import Jogo

def adicionar_jogo():
    jogos = []
    try:
        
        with open("jogo.json", "r") as arquivos:
            dados = json.load(arquivos)

            for item in dados:
                jogo = Jogo(
                    item["Nome"],
                    item["Genero"],
                    item["ano"]
                )
                jogos.append(jogo)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        
        pass
    return jogos


def salvar_jogo(listar_jogos):
    dados = []

    
    for jogo in listar_jogos:
        dados.append(jogo.para_dict())  

    with open("Jogo.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)