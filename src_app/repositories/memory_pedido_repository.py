from src_app.entities.pedido import Pedido
from src_app.gateways.pedido_gateway import IPedidoGateway
from src_app.frameworks.database.memory_database import MemoryDatabase

class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        self.database.pedidos.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

    def listar(self) -> list[Pedido]:
        return self.database.pedidos
