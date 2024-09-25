'''
Ejercicios de listas. Utilizar for, concatenación y creación de listas para resolver los
ejercicios a continuación. No usar funciones de python creadas por terceros.
Crear módulos para organizar las funciones y llamarlas desde el main.
1 - Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario
ordenar, se puede usar continue y resolver mediante programación estructurada
usando listas.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
e) Crear una función que permita recorrer las listas en ambos sentidos.
2- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = [“Juan”, “Matias”, “Carla”, “Susana”, “Olivia”, “Carlos”, “Daniel”, “Jimena”,
“Mariela”, “Ignacio”]
a) Devolver el nombre del respondiente más jóven y del más grande.
b) Usando break, busque en la lista si hay mayores de 65. En ese caso cortar la
iteración y mostrar mensaje por pantalla.
c) Utilizando continue, calcule la media etaria para mayores de 40 años
3- Programar un algoritmo que permita crear una nueva lista de respondentes de manera
secuencial. Deberán ingresar su nombre, sexo, cantidad de horas trabajadas e ingreso
semanal en listas separadas.
4- Desarrollar una función que calcule la media de ingresos por cuartil.
5- Realizar una función que permita corregir las listas del ejercicio 3 en caso de ser
necesario. Para ello se debe poder acceder a una posición particular y cargar nuevos
valores para el listado con valor incorrecto en dicha posición.
6 - Desarrollar una función que pida 10 números dentro de un rango especificado, validar
los números solicitados dentro de ese rango, guardar en una lista y retornarla. El programa
principal debe invocar a la función y mostrar por pantalla el retorno.
7- Dadas las siguientes listas:
Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas
de menor edad (puede ser más de una) y las retorne. El programa principal deberá mostrar
nombre y edad de los menores.
8- Desarrollar una función que verifique si todos los elementos de una lista son del mismo
tipo. En ese caso que devuelva el tipo que contiene, en caso contrario que informe qué tipos
de elementos contiene.
9- Desarrollar una función que permita cargar nuevos valores a una lista cualquiera. Se
debe poder validar el tipo de datos que contiene la lista.
'''


#  1
# a) Calcular el promedio del 20% que más gana
def promedio_top_20(lista_ingresos):
    # Calculamos  el número de elementos de la lista
    n = 0
    for _ in lista_ingresos:
        n += 1

    cantidad_top = n // 5  # El 20% de los elementos (división entera)
    suma_top = 0
    contador_top = 0

    # Encontrar el mayor ingreso de la lista 
    for _ in range(cantidad_top):
        maximo = lista_ingresos[0]
        for ingreso in lista_ingresos:
            if ingreso > maximo:
                maximo = ingreso
        
        # Sumar este valor y quitarlo temporalmente para encontrar el siguiente mayor
        suma_top += maximo
        contador_top += 1
        
        # Crear una nueva lista sin el valor máximo encontrado 
        nueva_lista = []
        encontrado = False
        for ingreso in lista_ingresos:
            if ingreso == maximo and not encontrado:
                encontrado = True
                continue
            nueva_lista = nueva_lista + [ingreso]  # Concatenamos el valor a la nueva lista
        lista_ingresos = nueva_lista

    if contador_top == 0:
        return 0
    return suma_top / contador_top

# b) Calcular el promedio de todos los ingresos
def promedio_todos(lista_ingresos):
    suma = 0
    contador = 0
    for ingreso in lista_ingresos:
        suma += ingreso
        contador += 1
    return suma / contador if contador > 0 else 0

# c) Buscar el valor que más se repite
def valor_mas_repetido(lista_ingresos):
    conteos = {}
    for ingreso in lista_ingresos:
        # Recorremos el diccionario 
        if ingreso in conteos:
            conteos[ingreso] += 1
        else:
            conteos[ingreso] = 1
    
    # Encontrar el valor con más repeticiones 
    max_repeticiones = 0
    for clave in conteos:
        if conteos[clave] > max_repeticiones:
            max_repeticiones = conteos[clave]

    valores_mas_repetidos = []
    for clave in conteos:
        if conteos[clave] == max_repeticiones:
            valores_mas_repetidos = valores_mas_repetidos + [clave]  # Concatenación 
    
    return valores_mas_repetidos

# d) Calcular la media geométrica 
def media_geometrica(lista_ingresos):
    producto_total = 1
    contador = 0
    for ingreso in lista_ingresos:
        producto_total *= ingreso
        contador += 1

    # Calcular la raíz enésima 
    if contador == 0:
        return 0

    
    raiz = producto_total ** (1 / contador)  

    return raiz

# e) Recorrer lista en ambos 
def recorrer_lista_ambos_sentidos(lista_ingresos):
    recorrido = []
    for ingreso in lista_ingresos:
        recorrido = recorrido + [ingreso]  # Concatenación 
    
    # Agregamos el recorrido inverso 
    n = 0
    for _ in lista_ingresos:
        n += 1

    for i in range(n - 1, -1, -1):  # Empezamos en el final
        recorrido = recorrido + [lista_ingresos[i]]  # Concatenación 
    
    return recorrido

lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

# a) Promedio del 20% que más gana
promedio_top = promedio_top_20(lista_ingresos)
print(f"Promedio del 20% que más gana: {promedio_top}")

# b) Promedio de todos los ingresos
promedio_total = promedio_todos(lista_ingresos)
print(f"Promedio de todos los ingresos: {promedio_total}")

# c) Valor que más se repite
valores_repetidos = valor_mas_repetido(lista_ingresos)
print(f"Valor(es) más repetido(s): {valores_repetidos}")

# d) Media geométrica
media_geom = media_geometrica(lista_ingresos)
print(f"Media geométrica: {media_geom}")

# e) Recorrer lista en ambos sentidos
recorrido = recorrer_lista_ambos_sentidos(lista_ingresos)
print(f"Lista recorrida en ambos sentidos: {recorrido}")


#  2

# a) Devolver el nombre del respondiente más joven y del más grande
def extremos_edad(lista_edad, lista_nombres):
    edad_min = lista_edad[0]
    edad_max = lista_edad[0]
    nombre_joven = lista_nombres[0]
    nombre_grande = lista_nombres[0]

    # Encontrar la edad mínima y máxima manualmente
    for i in range(1, len(lista_edad)):
        if lista_edad[i] < edad_min:
            edad_min = lista_edad[i]
            nombre_joven = lista_nombres[i]
        if lista_edad[i] > edad_max:
            edad_max = lista_edad[i]
            nombre_grande = lista_nombres[i]
    
    return nombre_joven, nombre_grande

# b) Usando break, buscar si hay mayores de 65 y cortar la iteración
def buscar_mayores_65(lista_edad, lista_nombres):
    for i in range(len(lista_edad)):
        if lista_edad[i] > 65:
            print(f"Se encontró un respondiente mayor de 65 años: {lista_nombres[i]} con {lista_edad[i]} años.")
            break
    else:
        print("No se encontró ningún respondiente mayor de 65 años.")

# c) Usando continue, calcular la media etaria para mayores de 40 años
def media_mayores_40(lista_edad):
    suma_edades = 0
    contador = 0

    for edad in lista_edad:
        if edad <= 40:
            continue  # Saltar a los que no son mayores de 40 años
        suma_edades += edad
        contador += 1
    
    if contador == 0:
        return 0
    return suma_edades / contador


lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

# a) Devolver el nombre del más joven y del más grande
nombre_joven, nombre_grande = extremos_edad(lista_edad, lista_nombres)
print(f"El más joven es {nombre_joven} y el más grande es {nombre_grande}")

# b) Buscar si hay mayores de 65 con break
buscar_mayores_65(lista_edad, lista_nombres)

# c) Calcular la media etaria para mayores de 40 años usando continue
media = media_mayores_40(lista_edad)
print(f"La media etaria de los mayores de 40 años es: {media}")

#  3
# Función para ingresar los datos de los respondentes secuencialmente
def ingresar_respondentes():
    lista_nombres = []
    lista_sexo = []
    lista_horas_trabajadas = []
    lista_ingreso_semanal = []
    
    while True:
        # Ingresar nombre
        nombre = input("Ingrese el nombre del respondente: ")
        lista_nombres = lista_nombres + [nombre]  
        
        # Ingresar sexo
        sexo = ""
        while sexo != "M" and sexo != "F":  # Validar que el sexo sea M o F
            sexo = input("Ingrese el sexo del respondente (M/F): ")
        lista_sexo = lista_sexo + [sexo]
        
        # Ingresar cantidad de horas trabajadas 
        horas_trabajadas = input("Ingrese la cantidad de horas trabajadas por semana: ")
        while not horas_trabajadas:  
            print("Por favor, ingrese un número entero válido.")
            horas_trabajadas = input("Ingrese la cantidad de horas trabajadas por semana: ")
        lista_horas_trabajadas = lista_horas_trabajadas + [int(horas_trabajadas)]
        
        # Ingresar ingreso semanal 
        ingreso_semanal = input("Ingrese el ingreso semanal: ")
        while not es_flotante(ingreso_semanal):  # Validar que sea un número flotante
            print("Por favor, ingrese un número válido.")
            ingreso_semanal = input("Ingrese el ingreso semanal: ")
        lista_ingreso_semanal = lista_ingreso_semanal + [float(ingreso_semanal)]
        
        # Preguntar si se desea agregar otro respondente
        continuar = input("¿Desea agregar otro respondente? (S/N): ")
        if continuar != 'S':
            break

    # Devolver todas las listas
    return lista_nombres, lista_sexo, lista_horas_trabajadas, lista_ingreso_semanal

# Función auxiliar para verificar si un valor es flotante
def es_flotante(valor):
    # Validamos si el valor puede ser un número flotante
    partes = valor.split(".")
    if len(partes) == 1:  # No tiene parte decimal, puede ser un entero
        return partes[0]
    elif len(partes) == 2:  # Tiene parte entera y decimal
        return partes[0] and partes[1]
    return False

# Llamar a la función para ingresar los datos
lista_nombres, lista_sexo, lista_horas_trabajadas, lista_ingreso_semanal = ingresar_respondentes()

# Mostrar los datos ingresados
print("\nDatos ingresados:")
for i in range(len(lista_nombres)):  # Recorremos las listas
    print(f"Respondente {i + 1}:")
    print(f"  Nombre: {lista_nombres[i]}")
    print(f"  Sexo: {lista_sexo[i]}")
    print(f"  Horas trabajadas: {lista_horas_trabajadas[i]}")
    print(f"  Ingreso semanal: {lista_ingreso_semanal[i]}")

#  4
# Función para calcular la media de ingresos por cuartil
def media_ingresos_por_cuartil(lista_ingresos):
    # Ordenar la lista de ingresos manualmente sin usar sorted()
    for i in range(len(lista_ingresos)):
        for j in range(i + 1, len(lista_ingresos)):
            if lista_ingresos[i] > lista_ingresos[j]:
                # Intercambiar los valores
                lista_ingresos[i], lista_ingresos[j] = lista_ingresos[j], lista_ingresos[i]
    
    # Dividir la lista en 4 cuartiles
    n = len(lista_ingresos)
    cuartiles = []
    tamaño_cuartil = n // 4  # División entera para obtener cuartiles más o menos iguales

    for i in range(4):
        cuartil = []
        for j in range(i * tamaño_cuartil, (i + 1) * tamaño_cuartil):
            if j < n:
                cuartil = cuartil + [lista_ingresos[j]]  # Agregar elementos al cuartil
        cuartiles = cuartiles + [cuartil]  # Agregar el cuartil a la lista de cuartiles

    # Si la división no es exacta, añadir los últimos elementos al último cuartil
    if len(cuartiles) > 0 and (n % 4 != 0):
        cuartiles[-1] = cuartiles[-1] + lista_ingresos[4 * tamaño_cuartil:]

    # Calcular la media para cada cuartil
    medias_cuartiles = []
    for cuartil in cuartiles:
        suma = 0
        contador = 0
        for ingreso in cuartil:
            suma += ingreso
            contador += 1
        if contador > 0:
            medias_cuartiles = medias_cuartiles + [suma / contador]
    
    return medias_cuartiles

# Lista de ingresos de ejemplo
lista_ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

# Calcular la media de ingresos por cuartil
medias_cuartiles = media_ingresos_por_cuartil(lista_ingresos)

# Mostrar el resultado
for i, media in enumerate(medias_cuartiles):
    print(f"Media del cuartil {i + 1}: {media}")


#  5
# Función para corregir un valor en una lista
def corregir_lista(lista_nombres, lista_sexo, lista_horas_trabajadas, lista_ingreso_semanal):
    while True:
        # Mostrar la lista de respondentes
        print("\nRespondentes actuales:")
        for i in range(len(lista_nombres)):
            print(f"{i + 1}. {lista_nombres[i]} - Sexo: {lista_sexo[i]} - Horas: {lista_horas_trabajadas[i]} - Ingreso: {lista_ingreso_semanal[i]}")
        
        # Solicitar al usuario la posición a corregir (restando 1 para acceder al índice correcto)
        posicion = input("\nIngrese el número del respondente que desea corregir (o 'salir' para finalizar): ")
        if posicion == "salir":
            break
        
        if not posicion or int(posicion) <= 0 or int(posicion) > len(lista_nombres):
            print("Por favor, ingrese una posición válida.")
            continue
        
        posicion = int(posicion) - 1  # Convertir a índice (0 basado)
        
        # Mostrar opciones de qué corregir
        print("\n¿Qué desea corregir?")
        print("1. Nombre")
        print("2. Sexo")
        print("3. Horas trabajadas")
        print("4. Ingreso semanal")
        opcion = input("Ingrese el número correspondiente a lo que desea corregir: ")

        # Corregir nombre
        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            lista_nombres[posicion] = nuevo_nombre

        # Corregir sexo (validación manual)
        elif opcion == "2":
            nuevo_sexo = ""
            while nuevo_sexo != "M" and nuevo_sexo != "F":
                nuevo_sexo = input("Ingrese el nuevo sexo (M/F): ")
            lista_sexo[posicion] = nuevo_sexo

        # Corregir horas trabajadas (validación manual)
        elif opcion == "3":
            nuevas_horas = input("Ingrese la nueva cantidad de horas trabajadas: ")
            while not nuevas_horas:
                print("Por favor, ingrese un número entero válido.")
                nuevas_horas = input("Ingrese la nueva cantidad de horas trabajadas: ")
            lista_horas_trabajadas[posicion] = int(nuevas_horas)

        # Corregir ingreso semanal (validación manual)
        elif opcion == "4":
            nuevo_ingreso = input("Ingrese el nuevo ingreso semanal: ")
            while not es_flotante(nuevo_ingreso):
                print("Por favor, ingrese un número válido.")
                nuevo_ingreso = input("Ingrese el nuevo ingreso semanal: ")
            lista_ingreso_semanal[posicion] = float(nuevo_ingreso)

        else:
            print("Opción no válida. Intente de nuevo.")

# Función auxiliar para verificar si un valor es flotante (la misma del ejercicio anterior)
def es_flotante(valor):
    partes = valor
    if len(partes) == 1:
        return partes[0]
    elif len(partes) == 2:
        return partes[0] and partes[1]
    return False

# Ingresar los datos de los respondentes
lista_nombres, lista_sexo, lista_horas_trabajadas, lista_ingreso_semanal = ingresar_respondentes()

# Llamar a la función para corregir cualquier valor incorrecto
corregir_lista(lista_nombres, lista_sexo, lista_horas_trabajadas, lista_ingreso_semanal)

# Mostrar los datos actualizados
print("\nDatos actualizados:")
for i in range(len(lista_nombres)):
    print(f"{i + 1}. Nombre: {lista_nombres[i]}, Sexo: {lista_sexo[i]}, Horas: {lista_horas_trabajadas[i]}, Ingreso semanal: {lista_ingreso_semanal[i]}")


#  6
# Función para pedir 10 números dentro de un rango especificado y validarlos
def pedir_numeros_en_rango(rango_min, rango_max):
    lista_numeros = []
    
    for i in range(10):  # Pedimos 10 números
        while True:
            numero = input(f"Ingrese el número {i + 1} dentro del rango ({rango_min}, {rango_max}): ")
            
            if not numero.isdigit():  # Verificar que sea un número entero
                print("Por favor, ingrese un número entero válido.")
                continue
            
            numero = int(numero)
            
            if numero < rango_min or numero > rango_max:  # Validar si está dentro del rango
                print(f"El número debe estar entre {rango_min} y {rango_max}. Intente de nuevo.")
            else:
                lista_numeros = lista_numeros + [numero]  # Agregar número a la lista
                break
    
    return lista_numeros

# Definir el rango
rango_min = 1
rango_max = 100

# Llamar a la función para pedir los números
lista_numeros = pedir_numeros_en_rango(rango_min, rango_max)

# Mostrar la lista de números ingresados
print("\nLista de números ingresados:")
print(lista_numeros)


#  7
# Función para encontrar las personas con la menor edad
def encontrar_menores_edad(nombres, edades):
    menores = []
    menor_edad = edades[0]  # Inicializamos con el primer valor de la lista

    # Encontrar la menor edad
    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad

    # Encontrar los nombres de las personas con la menor edad
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            menores = menores + [(nombres[i], edades[i])]  

    return menores

# Listas proporcionadas
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

# Llamar a la función para encontrar a los menores
menores = encontrar_menores_edad(nombres, edades)

# Mostrar los nombres y edades de las personas más jóvenes
print("Personas con la menor edad:")
for nombre, edad in menores:
    print(f"Nombre: {nombre}, Edad: {edad}")


#  8
# Función para verificar si todos los elementos de la lista son del mismo tipo
def verificar_tipos(lista):
    if len(lista) == 0: 
        return "La lista está vacía."
    
    tipo_base = type(lista[0])  
    tipos_presentes = set()  

    for elemento in lista:
        tipos_presentes.add(type(elemento))  

    # Verificamos si todos los tipos son iguales
    if len(tipos_presentes) == 1:
        return tipo_base  # Retornamos el tipo si todos son iguales
    else:
        return tipos_presentes  # Retornamos los tipos únicos en la lista

# Ejemplo de listas para probar la función
lista1 = [1, 2, 3, 4]  # Todos son enteros
lista2 = [1, 2.0, 3, 4]  # Mezcla de enteros y flotantes
lista3 = ["a", "b", "c"]  # Todos son cadenas
lista4 = []  # Lista vacía
lista5 = [1, "texto", 3.0]  # Mezcla de tipos

# Verificar cada lista
resultados = {
    "Lista 1": verificar_tipos(lista1),
    "Lista 2": verificar_tipos(lista2),
    "Lista 3": verificar_tipos(lista3),
    "Lista 4": verificar_tipos(lista4),
    "Lista 5": verificar_tipos(lista5),
}

# Mostrar los resultados
for nombre_lista, resultado in resultados.items():
    print(f"{nombre_lista}: {resultado}")


#  9
# Función para cargar nuevos valores a una lista validando el tipo de datos
def cargar_valores(lista):
    if len(lista) == 0:
        print("La lista está vacía. Se puede agregar cualquier valor.")
    
    tipo_lista = type(lista[0]) if len(lista) > 0 else None  # Obtener el tipo de la lista si no está vacía

    while True:
        nuevo_valor = input("Ingrese un nuevo valor (o 'salir' para finalizar): ")
        
        # Intentar convertir el valor a su tipo correspondiente
        if tipo_lista is int:
            try:
                nuevo_valor = int(nuevo_valor)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                continue
        elif tipo_lista is float:
            try:
                nuevo_valor = float(nuevo_valor)
            except ValueError:
                print("Por favor, ingrese un número decimal válido.")
                continue
        elif tipo_lista is str:
            nuevo_valor = str(nuevo_valor)  # Convertir a cadena (aunque ya es así)
        else:
            print("Tipo de lista no reconocido.")
            continue
        
        # Validar el tipo
        if tipo_lista is not None and type(nuevo_valor) != tipo_lista:
            print(f"El valor debe ser del tipo {tipo_lista.__name__}. Intente de nuevo.")
        else:
            lista.append(nuevo_valor)  # Agregar el valor a la lista
            print(f"Valor agregado: {nuevo_valor}")

        # Preguntar si desea seguir ingresando
        continuar = input("¿Desea agregar otro valor? (s/n): ")
        if continuar != 's':
            break

# Ejemplo de listas para probar la función
lista_enteros = [1, 2, 3]
lista_flotantes = [1.0, 2.5, 3.8]
lista_cadenas = ["a", "b", "c"]

# Cargar valores en cada lista
print("Cargando valores en la lista de enteros:")
cargar_valores(lista_enteros)

print("\nCargando valores en la lista de flotantes:")
cargar_valores(lista_flotantes)

print("\nCargando valores en la lista de cadenas:")
cargar_valores(lista_cadenas)

# Mostrar las listas finales
print("\nLista de enteros:", lista_enteros)
print("Lista de flotantes:", lista_flotantes)
print("Lista de cadenas:", lista_cadenas)