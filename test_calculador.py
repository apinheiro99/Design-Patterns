from unittest import TestCase

class Test_Calculador(TestCase):
    
    def test_Classe_Calculador_de_desconto(self):
        from Calculador_de_descontos import Calculador_de_descontos
        from Orcamento import Orcamento, Item

        orcamento = Orcamento()
        orcamento.adiciona_itens(Item('ITEM -1', 100))
        orcamento.adiciona_itens(Item('ITEM -2', 50)) 
        orcamento.adiciona_itens(Item('ITEM -3', 400))

        print ("Orçamento =", orcamento.valor)

        calculador = Calculador_de_descontos()
        desconto = calculador.calcula(orcamento)

        print ("Desconto calculado =", desconto)
        
        self.assertEqual(desconto, 38.50000000000001)

    def test_Classe_Calculador_de_imposto(self):
        from Calculador_de_impostos import Calculador_de_impostos
        from Orcamento import Orcamento, Item
        from Impostos import ISS, ICMS, ICPP, IKCV

        calculador = Calculador_de_impostos()
        orcamento = Orcamento()
        orcamento.adiciona_itens(Item('ITEM -1', 50))
        orcamento.adiciona_itens(Item('ITEM -2', 200)) 
        orcamento.adiciona_itens(Item('ITEM -3', 250))

        print("ISS e ICMS")
        self.assertEqual(calculador.realiza_calculo(orcamento, ISS()), 50.0)
        self.assertEqual(calculador.realiza_calculo(orcamento, ICMS()), 30.0)

        print("ISS + ICMS")
        self.assertEqual(calculador.realiza_calculo(orcamento, ISS(ICMS())), 80.0)
        
        print("ICPP e IKCV")
        self.assertEqual(calculador.realiza_calculo(orcamento, ICPP()), 25.0)
        self.assertEqual(calculador.realiza_calculo(orcamento, IKCV()), 30.0)

        print("ICPP + IKCV")
        self.assertEqual(calculador.realiza_calculo(orcamento, ICPP(IKCV())), 55.0)

    def test_orcamento(self):
        from Orcamento import Orcamento, Item #, Estado_de_um_orcamento, Em_aprovacao, Aprovado, Reprovado, Finalizado

        orcamento = Orcamento()
        orcamento.adiciona_itens(Item('ITEM -1', 100))
        orcamento.adiciona_itens(Item('ITEM -2', 50)) 
        orcamento.adiciona_itens(Item('ITEM -3', 400))

        print ("Orçamento =", orcamento.valor)
        self.assertEqual(orcamento.valor, 550.0)

        orcamento.aplica_desconto_extra()
        print ("Orcamento com desconto =", orcamento.valor)
        self.assertEqual(orcamento.valor,539.0)

        #Mudo de estado para aprovado e verifico o novo orcamento
        orcamento.aprova(orcamento)
        orcamento.aplica_desconto_extra()
        print ("Orcamento com desconto =", orcamento.valor)
        self.assertEqual(orcamento.valor, 512.05)

        #Mudo de estado para finalizado e verifico o novo orcamento
        orcamento.finaliza(orcamento)
        
        print ("Orcamento com desconto =", orcamento.valor)
        with self.assertRaises(Exception):
            orcamento.aplica_desconto_extra()
            orcamento.aprova(orcamento)
            orcamento.reprova(orcamento)
            orcamento.finaliza(orcamento)