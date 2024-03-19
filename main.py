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

def calcular_area_triangulo(base,altura):
    area = (base*altura)/2
    return area
    
def main():
    base = float(input("Ingresa la base del triangulo:  "))
    altura = float(input("Ingresa la altura del triangulo:  "))
    res = calcular_area_triangulo(base,altura)
    print(res)
    
main()
