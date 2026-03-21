import pytest
from validador_cep import validar_cep


@pytest.mark.parametrize("cep, cidade, esperado", [

    #válidos
    ("18110-000", "Votorantim", True),
    ("18110000", "Votorantim", True),
    ("18000-000", "Sorocaba", True),
    ("18000000", "Sorocaba", True),

    #case insensitive
    ("18110-000", "votorantim", True),
    ("18110-000", "VOTORANTIM", True)

    #inválidos
    ("18110-000", "Sorocaba", False),
    ("00000-000", "Cidade", False),
    ("abcde", "Sorocaba", False),

    #entradas inválidas
    ("", "Sorocaba", False),
    ("18000000", "", False),
    (None, "Sorocaba", False),

])
def test_validar_cep(cep, cidade, esperado):

    assert validar_cep(cep, cidade) == esperado