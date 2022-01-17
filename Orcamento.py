from abc import ABC, abstractmethod

class Estado_de_um_orcamento(ABC):

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception ("Orcamento em aprovacao nao pode ir para finalizado")

class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception ("Orcamento ja esta aprovado")

    def reprova(self, orcamento):
        raise Exception ("Orcamento aprovado nao pode ser reprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception ("Orcamentos reprovados nao recebem descontos extra")

    def aprova(self, orcamento):
        raise Exception ("Orcamento reprovado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception ("Orcamento ja esta reprovado")

    def finaliza(self, orcamento):
        Orcamento.estado_atual = Finalizado()

class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception ("Orcamentos finalizados nao recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception ("Orcamento finalizado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception ("Orcamento finalizado nao pode ser reprovado")

    def finaliza(self, orcamento):
        raise Exception ("Orcamento ja esta finalizado")

class Orcamento (object):
    
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
      
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
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print ("Orcamento com desconto =", orcamento.valor)

    #Mudo de estado para finalizado e verifico o novo orcamento
    orcamento.finaliza()
    orcamento.aplica_desconto_extra()
    print ("Orcamento com desconto =", orcamento.valor)