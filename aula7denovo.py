
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero."
    return x / y

def calculadora():
    print("Calculadora em Python")
    print("---------------------")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    if escolha == '1':
        print("Resultado:", somar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida.")

def menu():
    esc1 = input('voce deseja jogar ou calcular: ')
    if esc1 == 'jogar' :
        adivinhacao()
    if esc1 == 'calcular' :
        calculadora()


def adivinhacao():
    import random 
    
    
    num = random.randint(1, 100)
    
    
    
    while 1:
        
        palpite = input('Digite um numero: ')
        palpite = int (palpite)
        if palpite  ==  num:
            print ('ganhou')
            break
        elif palpite < num:
            print('numero maior')
        elif palpite > num:
            print ('numero menor')
        
      

menu()
