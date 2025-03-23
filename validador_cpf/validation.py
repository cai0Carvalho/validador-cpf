from utils import clean_cpf

class CPFValidator():

    def __init__(self, cpf: str):
        """Inicializa a classe limpando o CPF, removendo caracteres não numéricos."""
        self.cpf = clean_cpf(cpf)
    
    def validate(self) -> bool:
        """Executa todas as validações e retorna True se o CPF for válido, False caso contrário."""
        if not self.lenth_cpf(): 
            return False

        if not self.is_sequence(): 
            return False

        if not self.first_digit_validate():
            return False
        
        if not self.second_digit_validate():
            return False
        
        return True
    
    """Verifica se o CPF possui exatamente 11 dígitos."""
    def lenth_cpf (self) -> bool:
        return len(self.cpf) == 11
    
    """Verifica se todos os dígitos do CPF são iguais (ex: 111.111.111-11)."""
    def is_sequence(self) -> bool:
        return self.cpf == self.cpf[0] * len(self.cpf)
    
    def digits_validate(self, digits_verification) -> int:
        """
        Calcula os dígitos verificadores do CPF.
        
        Parâmetros:
        - digits_verification (int): Define se é o primeiro (10) ou segundo (11) dígito.

        Retorna:
        - O valor correto do dígito verificador calculado.
        """
        total_sum = 0
        mult = digits_verification
        cpf_num = self.cpf[:mult-1]

        for digit in cpf_num:
            total_sum = int(digit)*mult
            mult -= 1

        return 0 if total_sum % 11 < 2 else 11 - (total_sum % 11)

    """Valida o primeiro dígito verificador (posição 9 do CPF)."""
    def first_digit_validate (self) -> int:
         first_dig = 10 
         return self.digits_validate(10) == int(self[9])

    """Valida o segundo dígito verificador (posição 10 do CPF)."""
    def second_digit_validate (self) -> int:
         first_dig = 11
         return self.digits_validate(11) == int(self[10])
    
