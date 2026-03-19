import re

def validar_cep(cep, cidade):
    if not cep or not cidade:
        return False

    cep = re.sub(r"\D", "", cep)

    if len(cep) != 8:
        return False

    base_ceps = {
        "18110000": "Votorantim",
        "18000000": "Sorocaba"
    }

    if cep in base_ceps:
        return base_ceps[cep].strip().lower() == cidade.strip().lower()

    return False
