class Orcamento (object):
    
    EM_APROVACAO = 1
    APROVADO = 2
    REPROVADO = 3
    FINALIZADO = 4


    def __init__(self):
        self.__itens = []
        self.estado_atual = Orcamento.EM_APROVACAO
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        if self.estado_atual == Orcamento.EM_APROVACAO:
            self.__desconto_extra += self.valor * 0.02
        elif self.estado_atual == Orcamento.APROVADO:
            self.__desconto_extra += self.valor * 0.05
        elif self.estado_atual == Orcamento.REPROVADO:
            raise Exception ("Orcamentos reprovados nao recebem descontos extra")
        elif self.estado_atual == Orcamento.FINALIZADO:
            raise Exception ("Orcamentos finalizados nao recebem desconto extra")
      
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_itens(self, item):
        self.__itens.append(item)

class Item(object):
    
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

#Testa a classe dentro dela mesma
if __name__ == "__main__":

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('ITEM -1', 100))
    orcamento.adiciona_itens(Item('ITEM -2', 50)) 
    orcamento.adiciona_itens(Item('ITEM -3', 400))

    print ("Orçamento =", orcamento.valor)

    orcamento.aplica_desconto_extra()
    print ("Orcamento com desconto =", orcamento.valor)

    #Mudo de estado para aprovado e verifico o novo orcamento
    orcamento.estado_atual = Orcamento.APROVADO
    orcamento.aplica_desconto_extra()
    print ("Orcamento com desconto =", orcamento.valor)

    #Mudo de estado para finalizado e verifico o novo orcamento
    orcamento.estado_atual = Orcamento.FINALIZADO
    orcamento.aplica_desconto_extra()
    print ("Orcamento com desconto =", orcamento.valor)