from src.models.desconto import IDesconto

class Pedido:
    def __init__(self):
        self.descontos: list[IDesconto] = []
        self.valor_total: float = 0.0
        self.valor_original = 0.0

    def valor_final (self,valor) -> float:
        self.valor_original = valor
        return self.valor_original - self.descontos[0].calcular(self.valor_original)