from typing import List
from src_app.entities.pedido import Pedido

class MemoryDatabase:
    """Banco de dados em memória (simula persistência)"""
    
    def __init__(self):
        self.pedidos: List[Pedido] = []

    def salvar(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)

    def listar(self) -> List[Pedido]:
        return self.pedidos
