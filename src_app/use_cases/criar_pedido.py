from src_app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src_app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO
from src_app.entities.pedido import Pedido
from src_app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src_app.gateways.pedido_gateway import IPedidoGateway


class CriarPedido:
    """Use Case - Responsável por criar um pedido aplicando o desconto correto."""

    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        # Escolhe o tipo de desconto
        tipo = input_dto.tipo_desconto.lower().strip()
        if tipo == "vip":
            desconto = DescontoVIP()
        elif tipo == "premium":
            desconto = DescontoPremium()
        else:
            desconto = DescontoNormal()

        # Cria o pedido
        pedido = Pedido(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            desconto=desconto
        )

        # Salva (sem passar tipo_desconto, pois o repositório atual não suporta)
        self.pedido_gateway.salvar(pedido)

        # Retorna o Output DTO
        return CriarPedidoOutputDTO(
            cliente=pedido.cliente,
            valor_original=pedido.valor_original,
            valor_desconto=pedido.valor_desconto(),
            valor_final=pedido.valor_final(),
            tipo_desconto=input_dto.tipo_desconto
        )

    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        """Lista todos os pedidos convertendo para OutputDTO."""
        pedidos = self.pedido_gateway.listar()
        lista_dto = []

        for pedido in pedidos:
            dto = CriarPedidoOutputDTO(
                cliente=pedido.cliente,
                valor_original=pedido.valor_original,
                valor_desconto=pedido.valor_desconto(),
                valor_final=pedido.valor_final(),
                tipo_desconto="normal"  # se quiser salvar o tipo, teria que alterar o repositório
            )
            lista_dto.append(dto)

        return lista_dto