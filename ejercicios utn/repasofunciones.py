'''
Repaso funciones
1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.
'''
#1
import math
#a
def area_circulo(radio=3):
    "Calcula el área de un círculo con un radio dado. Si no se especifica, el radio por defecto es 3."
    return math.pi * radio ** 2
#b
def area_cuadrado(lado):
    "Calcula el área de un cuadrado con el lado dado."
    return lado ** 2
#c
def area_triangulo(base, altura):
    "Calcula el área de un triángulo dado su base y altura."
    return (base * altura) / 2

#2
import math
#a
def perimetro_circulo(radio=3):
    "Calcula el perímetro de un círculo con un radio dado. Si no se especifica, el radio por defecto es 3."
    return 2 * math.pi * radio
#b
def perimetro_cuadrado(lado):
    "Calcula el perímetro de un cuadrado con el lado dado."
    return 4 * lado
#c
def perimetro_triangulo(lado1, lado2, lado3):
    "Calcula el perímetro de un triángulo dados sus tres lados."
    return lado1 + lado2 + lado3
