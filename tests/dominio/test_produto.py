from caixa.dominio.produto import Produto

def test_baixar_estoque_reduz_quantidade():
    p = Produto("Forma Bolo", 1500, 10)
    p.baixar_estoque(3)
    assert p.quantidade == 7