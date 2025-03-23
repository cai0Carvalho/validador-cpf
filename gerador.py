class validation():
    
    def validate() -> bool:
        clean_cpf = validation.clean_cpf(cpf)

        if not validation.lenth_cpf(clean_cpf):
            return False

        if not validation.is_sequence(clean_cpf):
            return False

        if not validation.first_digit_validate(clean_cpf):
            return False
        
        if not validation.second_digit_validate(clean_cpf):
            return False
        
        return True

    # Função para limpar os dígitos do cpf
    def clean_cpf(cpf: str) -> str:
        clean_cpf = ''
        for digit in cpf:
            if digit.isdigit():
                clean_cpf += digit
            return clean_cpf
        
    # Função para validar tamanho
    def lenth_cpf (cpf: str) -> bool:
        return len(cpf) == 11
    
    # Função para verificar se o cpf é uma sequencia repetida
    def is_sequence(cpf: str) -> bool:
        return (cpf[0]*len(cpf)) == cpf
    
    # Função para validar dígitos
    def digits_validate(cpf: str, digits_verification) -> int:
        total_sum = 0
        mult = digits_verification
        cpf_num = cpf[:mult-1]

        for digit in cpf_num:
            total_sum = (int(digit)*mult)
            mult -= 1

        if total_sum % 11 < 2:
            return 0
        else: 
            return 11 - (total_sum % 11)


    def first_digit_validate (cpf: str) -> int:
         first_dig = 10
         return validation.digits_validate(cpf, first_dig) == int(cpf[9])
    
    def second_digit_validate (cpf: str) -> int:
         first_dig = 11
         return validation.digits_validate(cpf, first_dig) == int(cpf[10])
    
