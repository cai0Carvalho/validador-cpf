## Validador de CPF - Projeto Python
Este projeto é um Validador de CPF desenvolvido em Python, com o objetivo de realizar a verificação completa e detalhada de um CPF informado. O validador aplica diversas validações, incluindo a verificação de caracteres não numéricos, tamanho correto, sequências repetidas, e o cálculo dos dígitos verificadores, conforme as regras oficiais.

## Funcionalidades
- Este validador realiza as seguintes verificações no CPF:

- Limpeza dos caracteres não numéricos: Remove automaticamente qualquer ponto, traço ou espaço, permitindo que o CPF seja informado com ou sem formatação.

- Validação do tamanho correto: Verifica se o CPF possui exatamente 11 dígitos, conforme o formato oficial.

- Detecção de sequências repetidas: Identifica e rejeita CPFs compostos por sequências repetidas, como "111.111.111-11" ou "222.222.222-22", que são inválidos por padrão.

- Cálculo e verificação dos dígitos verificadores: Realiza os cálculos para validar os dois últimos dígitos do CPF, que são usados para garantir sua autenticidade.

## Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

- `main.py`: Arquivo de execução do projeto, que solicita o CPF ao usuário, chama o validador e imprime o resultado da validação.

-`validation.py`: Contém a classe CPFValidator, que implementa a lógica de validação e cálculo dos dígitos verificadores.

-`utils.py`: Função auxiliar para limpeza do CPF, removendo caracteres não numéricos.


## Instalação e Execução

1. Clone o repositório:
    ```bash 
    git clone https://github.com/cai0Carvalho/validador-cpf.git
    ```
2. Acesse o diretório do projeto:
    ``` bash
    cd validador-cpf
    ```
3. Execute o programa:
    ``` bash
    python main.py
    ```

Autor:
Caio Carvalho

caiocamorim123@gmail.com
(https://www.linkedin.com/in/caio-c%C3%A9sar-8791772b8/).