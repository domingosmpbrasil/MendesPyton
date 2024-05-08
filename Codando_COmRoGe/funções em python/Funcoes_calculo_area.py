import soundfile




# criar funções de calculo de área





# calculo da área de um quadrado

def calcula_quadrado(lado):
    calculo = lado ** 2
    return round(calculo, 2)




# calculo da área de um triangulo, especifique os tipos de triangulos

def tipo_triangulos(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return print("é um triángulo equilátero")

    if lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        return print("Esse triângulo é isóscilis")

    if lado1 != lado2 and lado3 != lado1:
        return print("Esse triângulo é escaleno.")






tipo_triangulos(4, 3, 6)


