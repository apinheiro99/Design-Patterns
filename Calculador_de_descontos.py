class Calculador_de_descontos(object):

    def calcula(orcamento):
        if orcamento.total_de_items > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07