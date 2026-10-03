from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco_centavos: int
    quantidade: int

    def baixar_estoque(self, quantidade: int) -> None:
        self.quantidade -= quantidade