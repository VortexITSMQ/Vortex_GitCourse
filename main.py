
def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

num1 = 5
num2 = 10
resultado = multiplicar(num1, num2)
print("El resultado de la multiplicación es:", resultado)

# piramide

def piramide(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))

piramide(5)

