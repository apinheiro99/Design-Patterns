from Descontos import *

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens().calcula(orcamento)
        if desconto == 0:
            desconto = Desconto_por_mais_de_quinheiros_reais().calcula(orcamento)
        return desconto

#Testa a classe dentro dela mesma
if __name__ == "__main__":

    from Orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('ITEM -1', 100))
    orcamento.adiciona_itens(Item('ITEM -2', 50)) 
    orcamento.adiciona_itens(Item('ITEM -3', 400))

    print ("Orçamento =", orcamento.valor)

    calculador = Calculador_de_descontos()
    desconto = calculador.calcula(orcamento)

    print ("Desconto calculado =", desconto)