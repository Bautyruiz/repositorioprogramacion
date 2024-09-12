"""Parte A
1 - Crear una función que muestre por pantalla el número que recibe como parámetro.
2 - Crear una función que permita determinar si un número es par o no. La función retorna
“True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
realizando la invocación o llamada.
3 - Especializar la función del punto 1 para que valide el número en un rango determinado
pasado por parámetro “desde”-“hasta”.
4 - Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en
sus 4 combinaciones.
restar1(int, int)->int:
restar2()->int:
restar3(int, int):
restar4():
5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
reutilizarse funciones ya creadas.
6 - Realizar un programa que: asigne a las variables numero1 y numero2 los valores
solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
a través de una función. Mostrar el resultado por pantalla.
Parte B
Ejercicio 7:
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
= 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente.
Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.
Ejercicio 9:
Genere un paquete con ambos módulos.
Ejercicio 10:
Subir a github el paquete.
"""
#1
def mostrar_numero(numero):
    print(f"El número es: {numero}")

2#
def definir_par(numero : int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
def definir_par_validado(numero : int, desde : int, hasta : int):
    if numero < desde or numero > hasta:
        print("el numero ingresado no estaa dentro del rango especifico")
    else:
        if numero %2 == 0:
            print(True)
        else:
            print(False)

#3
def mostrar_numero_en_rango(numero, desde, hasta):
    if desde <= numero <= hasta:
        print(f"El número {numero} está dentro del rango [{desde}, {hasta}]")
    else:
        print(f"El número {numero} está fuera del rango [{desde}, {hasta}]")

#4
def reanudar_1(numero_1:int, numero_2:int)-> int:
    return numero_1 - numero_2

def reanudar_2()-> int:
    return 20 - 5

def reanudar_3(numero_1, numero_2)-> int:
    print(numero_1 - numero_2) 

def reanudar_4():
    print(20 - 5)
#5
def realizar_descuento(valor):
    return valor * 0.95

numero1 = int(input("Ingrese un valor entre 10 y 100: "))
if 10 <= numero1 <= 100:
    numero_con_descuento = realizar_descuento(numero1)
    print(f"El valor con el descuento aplicado es: {numero_con_descuento}")
else:
    print("El número no está en el rango.")

#6
def operar_numeros(a, b, operacion):
    if operacion == 's':
        return a + b
    elif operacion == 'r':
        return a - b
    else:
        return None

numero1 = int(input("Ingrese un valor entre 10 y 100: "))
numero2 = int(input("Ingrese otro valor entre 10 y 100: "))
if 10 <= numero1 <= 100 and 10 <= numero2 <= 100:
    operacion = input("Ingrese 's' para sumar o 'r' para restar: ")
    if operacion in ['s', 'r']:
        resultado = operar_numeros(numero1, numero2, operacion)
        print(f"El resultado de la operación es: {resultado}")
    else:
        print("Operación no válida.")
else:
    print("Uno o ambos números no están en el rango.")

#7
def calcular_impuesto_nacional(valor_ventas_nacionales, iva=21):
    """Calcula el valor neto de ventas nacionales sin IVA."""
    return valor_ventas_nacionales / (1 + (iva / 100))

def calcular_impuesto_exportaciones(valor_exportaciones, retenciones=15):
    """Calcula el valor de exportaciones después de retenciones."""
    return valor_exportaciones * (1 - (retenciones / 100))

def calculo_total_impuestos(valor_exportaciones, valor_ventas_nacionales, iva=21, retenciones=15):
    """Calcula el total de impuestos sumando ventas nacionales y exportaciones."""
    total_nacional = calcular_impuesto_nacional(valor_ventas_nacionales, iva)
    total_exportaciones = calcular_impuesto_exportaciones(valor_exportaciones, retenciones)
    return total_nacional + total_exportaciones

#8
def calcular_salario(horas_trabajadas, anios_antiguedad):
    """Calcula el salario según horas trabajadas y antigüedad."""
    salario_base = horas_trabajadas * 10
    bono_antiguedad = salario_base * (0.03 * anios_antiguedad)
    return salario_base + bono_antiguedad

def calcular_productividad(artefactos_producidos, horas_trabajadas):
    """Calcula la productividad como artefactos producidos por hora."""
    if horas_trabajadas == 0:
        return 0
    return artefactos_producidos / horas_trabajadas

def reporte_empleado(nombre, edad, horas_trabajadas, anios_antiguedad, artefactos_producidos):
    """Genera un reporte con la información del empleado."""
    salario = calcular_salario(horas_trabajadas, anios_antiguedad)
    productividad = calcular_productividad(artefactos_producidos, horas_trabajadas)
    return (f"Nombre: {nombre}\nEdad: {edad}\nSalario: {salario}\nProductividad: {productividad}")