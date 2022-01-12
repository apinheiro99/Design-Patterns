class Calculador_de_descontos(object):

    def calcula(orcamento):
        if orcamento.total_de_items > 5:
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

    print (orcamento.valor)