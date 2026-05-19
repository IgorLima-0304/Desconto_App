from src_app.entities.desconto import IDesconto


class Pedido:
    """Entidade que representa um Pedido no domínio da aplicação."""

    def __init__(self, cliente: str, valor_original: float, desconto: IDesconto):
        self.cliente = cliente
        self.valor_original = valor_original
        self.desconto = desconto

    def valor_desconto(self) -> float:
        """Calcula o valor do desconto aplicado."""
        return self.desconto.calcular(self.valor_original)

    def valor_final(self) -> float:
        """Retorna o valor final do pedido após aplicar o desconto."""
        return self.valor_original - self.valor_desconto()
