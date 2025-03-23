 # Função para limpar os dígitos do cpf
def clean_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))