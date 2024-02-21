# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("\nSelecione o número da operação desejada:")
print("\n1 - Soma")
print("\n2 - Subtração")
print("\n3 - Multiplicação")
print("\n4 - Divisão")

# input de qual a operação que será realizada
op = int(input("\nDigite sua opção (1|2|3|4): "))

# op. soma
if(op == 1):
    num1soma = float(input("\nDigite o primeiro número: "))
    num2soma = float(input("\nDigite o segundo número: "))
    resultsoma = num1soma + num2soma
    print("%.2f + %.2f = %.2f" %(num1soma,num2soma,resultsoma))

# op. subtração
elif(op == 2):
    num1sub = float(input("\nDigite o primeiro número: "))
    num2sub = float(input("\nDigite o segundo número: "))
    resultsub = num1sub - num2sub
    print("%.2f - %.2f = %.2f" %(num1sub,num2sub,resultsub))

# op. multiplicação
elif(op == 3):
    num1mul = float(input("\nDigite o primeiro número: "))
    num2mul = float(input("\nDigite o segundo número: "))
    resultmul = num1mul * num2mul
    print("%.2f * %.2f = %.2f" %(num1mul,num2mul,resultmul))

# op. divisão
elif(op == 4):
    num1div = float(input("\nDigite o primeiro número: "))
    num2div = float(input("\nDigite o segundo número: "))
    if(num2div == 0):
        print("\nTa louco? Não existe divisão por zero mané")
    resultdiv = num1div / num2div
    print("%.2f / %.2f = %.2f" %(num1div,num2div,resultdiv))

# se não for nenhum dos 4 números
else:
    print("\nOpção inválida!!")