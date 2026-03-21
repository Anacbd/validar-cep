import re

def validar_cep(cep, cidade):
    if not cep or not cidade:
        return False

    # remove caracteres não numéricos
    cep = re.sub(r"\D", "", cep)

    # verifica se tem 8 dígitos
    if len(cep) != 8:
        return False

    # base simples de CEPs
    base_ceps = {
        "18110000": "Votorantim",
        "18000000": "Sorocaba"
    }

    if cep in base_ceps:
        return base_ceps[cep].strip().lower() == cidade.strip().lower()

    return False