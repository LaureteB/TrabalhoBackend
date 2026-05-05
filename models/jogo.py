class Jogo:
    def __init__(self, nome, genero, ano):

        self.__nome = nome
        self.__genero = genero
        self.__ano = ano


    @property
    def nome (self):
        return self.__nome
    

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Nome Inválido!")
        else:
            self.__nome = novo_nome



    def exibir(self):
        self.__log()
        print("Nome: ",self.__nome)
        print("Genero: ",self.__genero)
        print("Ano: ",self.__ano)

    def __log(self):
        print("(LOG) Jogo Acessado")



    def para_dict(self):
        return {
            "nome":self.__nome,
            "genero":self.__genero,
            "ano":self.__ano,
        }


    @staticmethod
    def catergotia_padrao():
        return "Jogo"