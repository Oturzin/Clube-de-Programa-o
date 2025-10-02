def quadrado():
    lado = int(input("digite o valor do lado"))
    area  = lado * lado
    return area

def retangulo():
    lado = int(input("digite o valor do lado"))
    altura = int(input("digite o valor da altura"))
    area  = lado * altura
    return area
    
def  triangulo():
    lado = int(input("digite o valor do lado"))
    altura = int(input("digite o valor da altura"))
    area  = lado * altura /2
    return area

def circulo():
    raio = int(input('digite o valor do raio: '))
    area = (3.14 *raio)**2
    return area
    
def trapezio():
    b = int(input('Base menor: '))
    bM = int(input('Base maior: '))
    h = int(input('altura: '))
    area = (b + bM) * h / 2
    return area
    



print("Calculadora de areas")
print("a - Quadrado")
print("b - retangulo")
print("c - Triangulo")
print("d - circulo")
print("e - Trapezio")

opcao = input("Escolha uma opcao: ")

if opcao == 'a':
    area=quadrado()
    lado = int(input("digite o valor do lado"))
    area  = lado * lado
    
    
    
elif  opcao == "b":
    b = int(input('Numero da base: '))
    h = int(input('Numero da altura: '))
    print(f'O resultado C) {b *h}')

elif opcao == "c":
    b = int(input('Numero da base: '))
    h = int(input('Numero da altura: '))
    print(f'O resultado é {b *h/ 2 }')  

