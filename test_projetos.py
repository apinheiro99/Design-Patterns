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

    def test_Classe_Nota_fiscal(self):

        from datetime import date
        from Nota_fiscal import Item, Nota_fiscal
        
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

        self.assertEqual(nota_fiscal.razao_social, "FHSA Limitada")
        self.assertEqual(nota_fiscal.cnpj, "012345678901234")
        self.assertEqual(nota_fiscal.itens, "(Item A, 100) (Item B, 200) ")
        self.assertEqual(nota_fiscal.data_de_emissao, date.today())
        self.assertEqual(nota_fiscal.detalhes, "")

    def test_Classe_Criador_de_nota_fiscal(self):

        from datetime import date
        from Nota_fiscal import Item
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

        # Utilizando o Design Pattern Builder
        nota_fiscal_criada_com_builder = (Criador_de_nota_fiscal()
                                        .com_razao_social("FHSA Limitada")
                                        .com_cnpj("012345678901234")
                                        .com_itens(itens)
                                        .constroi()
                                        )

        print(nota_fiscal_criada_com_builder)

        self.assertEqual(nota_fiscal_criada_com_builder.razao_social, "FHSA Limitada")
        self.assertEqual(nota_fiscal_criada_com_builder.cnpj, "012345678901234")
        self.assertEqual(nota_fiscal_criada_com_builder.itens, "(Item A, 100) (Item B, 200) ")
        self.assertEqual(nota_fiscal_criada_com_builder.data_de_emissao, date.today())
        self.assertEqual(nota_fiscal_criada_com_builder.detalhes, "")

    def test_Observador(self):

        from datetime import date
        from Nota_fiscal import Item, Nota_fiscal
        from Observadores import imprime, envia_por_email, salva_no_banco
        
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
            itens = itens,
            observadores =  [imprime, envia_por_email, salva_no_banco, salva_no_banco]
        )

        print(nota_fiscal)

        self.assertEqual(nota_fiscal.razao_social, "FHSA Limitada")
        self.assertEqual(nota_fiscal.cnpj, "012345678901234")
        self.assertEqual(nota_fiscal.itens, "(Item A, 100) (Item B, 200) ")
        self.assertEqual(nota_fiscal.data_de_emissao, date.today())
        self.assertEqual(nota_fiscal.detalhes, "")
        self.assertEqual(nota_fiscal.observadores, [imprime, envia_por_email, salva_no_banco, salva_no_banco])