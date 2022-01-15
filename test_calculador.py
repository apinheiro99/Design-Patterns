from unittest import TestCase
# from Descontos import *
from Orcamento import *
from Calculador_de_descontos import *

class Test_Calculador(TestCase):
    
    def test_Classe_Calculador_de_desconto(self):

        orcamento = Orcamento()
        orcamento.adiciona_itens(Item('ITEM -1', 100))
        orcamento.adiciona_itens(Item('ITEM -2', 50)) 
        orcamento.adiciona_itens(Item('ITEM -3', 400))

        print ("Orçamento =", orcamento.valor)

        calculador = Calculador_de_descontos()
        desconto = calculador.calcula(orcamento)

        print ("Desconto calculado =", desconto)
        
        self.assertEqual(desconto, 38.50000000000001)
