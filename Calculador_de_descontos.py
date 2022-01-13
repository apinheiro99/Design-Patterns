class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07

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