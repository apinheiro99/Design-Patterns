from Impostos import ICPP, IKCV, ISS, ICMS

class Calculador_de_impostos (object):
    
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print (imposto_calculado)
        return imposto_calculado

#Testa a classe dentro dela mesma
if __name__ == "__main__":
    from Orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()
    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('ITEM -1', 50))
    orcamento.adiciona_itens(Item('ITEM -2', 200)) 
    orcamento.adiciona_itens(Item('ITEM -3', 250))

    print("ISS e ICMS")
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print("ICPP e IKCV")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
