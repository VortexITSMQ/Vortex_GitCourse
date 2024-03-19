def calcular_area_triangulo(base,altura):
    area = (base*altura)/2
    return area
    
def main():
    base = float(input("Ingresa la base del triangulo:  "))
    altura = float(input("Ingresa la altura del triangulo:  "))
    res = calcular_area_triangulo(base,altura)
    print(res)
    
main()