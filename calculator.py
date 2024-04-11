# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("\nSelecione o número da operação desejada:")
print("\n1 - Soma")
print("\n2 - Subtração")
print("\n3 - Multiplicação")
print("\n4 - Divisão")

# input de qual a operação que será realizada
op = int(input("\nDigite sua opção (1|2|3|4): "))

# op. soma
if(op == 1):
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    print("\n")
    print(num1, "+", num2, "=", add(num1,num2))
    print("\n")

# op. subtração
elif(op == 2):
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    print("\n")
    print(num1, "-", num2, "=", subtract(num1,num2))
    print("\n")

# op. multiplicação
elif(op == 3):
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    print("\n")
    print(num1, "*", num2, "=", multiply(num1,num2))
    print("\n")

# op. divisão
elif(op == 4):
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    if(num2 == 0):
        print("\nNão existe divisão por zero!!")
    print("\n")
    print(num1, "/", num2, "=", divide(num1,num2))
    print("\n")

# se não for nenhum dos 4 números
else:
    print("\nOpção inválida!!")