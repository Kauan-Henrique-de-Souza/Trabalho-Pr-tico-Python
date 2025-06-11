saida = ''

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

# Laço principal
while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação desejada (+, -, *, / ou nome): ')
        
        resultado = calculadora(num1, num2, operacao)
        print('Resultado da operação:', resultado)
    except ValueError:
        print('Entrada inválida. Por favor, digite apenas números válidos.')

    saida = input('Deseja continuar? (S/N): ')
