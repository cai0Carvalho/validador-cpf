from validation import CPFValidator

if __name__ == "__main__":
    cpf = input("Digite o CPF: ")
    validator = CPFValidator(cpf)


    if validator.validate():
        print("CPF válido")
    else:
        print("CPF inválido")
