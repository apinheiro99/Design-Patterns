from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao (self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao = date.today(), detalhes = ""):
        self.__razao_social = razao_social
        self.__cnpf =cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception ("Detalhes da nota nao podem ter mais do que 20 caracteres")
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpf

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        string = ""
        for item in self.__itens:
            string += "(" + item.descricao + ", " + str(item.valor) +") "
        return string

    def __str__(self):
        return ("++++++++++++++++++++"  + "\n"
                    + "Razao social: " + self.razao_social + "\n"
                    + "CNPJ: " + self.cnpj + "\n"
                    + "Itens: " + self.itens + "\n"
                    + "Data de emissao: " + str(self.data_de_emissao) + "\n"
                    + "Detalhes: " + self.detalhes + "\n"
                    + "++++++++++++++++++++"  + "\n"
        )

if __name__ == "__main__":
    
    from Criador_de_nota_fiscal import Criador_de_nota_fiscal

    itens = [
        Item(
            "Item A",
            100
        ),
        Item(
            "Item B",
            200
        )
    ]

    # Nomeando variaveis utilizacao do Design Pattern Builder ja do proprio Python (nao importa a ordem dos parametros)
    nota_fiscal = Nota_fiscal(
        cnpj = "012345678901234",
        razao_social = "FHSA Limitada",
        data_de_emissao = date.today(),
        detalhes = "",
        itens = itens
    )

    print(nota_fiscal)

    # Utilizando o Design Pattern Builder
    nota_fiscal_criada_com_builder = (Criador_de_nota_fiscal()
                                    .com_razao_social("FHSA Limitada")
                                    .com_cnpj("012345678901234")
                                    .com_itens(itens)
                                    .constroi()
                                    )

    print(nota_fiscal_criada_com_builder)