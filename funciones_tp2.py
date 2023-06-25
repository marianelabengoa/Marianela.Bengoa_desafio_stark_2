from data_stark import *
import os

#              opcion 0                 #
def nueva_lista(lista1:list, lista2:list)->list:
    for elemento in lista1:
        lista2.append(elemento)
    return lista2

def stark_normalizar_datos(lista: list, primera_key: str, tipo) -> None:
    for personaje in lista:
        if type(personaje[primera_key])!=tipo:
            personaje[primera_key] = tipo(personaje[primera_key])


#              opcion 1                 #

def obtener_nombre(heroe:dict)->str:
    nombre = heroe['nombre']
    nombre_formateado = "Nombre: " + nombre
    return nombre_formateado

def imprimir_dato(dato)->None:
    print(dato)

def stark_imprimir_nombres_heroes(lista:list):
    if len(lista)>0:
        for heroe in lista:
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)
    else:
        return -1



#              opcion 2                 #
def obtener_nombre_y_dato(heroe:dict, key:str)->str:
    nombre = heroe['nombre']
    dato = heroe[key]
    nombre_y_dato=f"Nombre: {nombre:18s} | {key}: {dato}"
    return nombre_y_dato

def stark_imprimir_nombres_alturas(lista:list)->None:
    if len(lista)>0:
        for heroe in lista_personajes:
            nombre_altura=obtener_nombre_y_dato(heroe, "altura")
            print(nombre_altura)
    else:
        return -1


#              opcion 3,4,6,7                 #
def calcular_max(lista: list, primer_key: str) -> str:
    flag = False
    for personaje in lista:
        if (flag == False):
            personaje_mayor = personaje[primer_key]
            nom_personaje_mayor = personaje['nombre']
            flag = True

        elif (personaje[primer_key] > personaje_mayor):
            personaje_mayor = personaje[primer_key]
            nom_personaje_mayor = personaje['nombre']
    mayor=f"{personaje_mayor}, {nom_personaje_mayor}"
    return nom_personaje_mayor,personaje_mayor

def calcular_min(lista: list, primer_key: str) -> str:
    flag_altura = False
    for personaje in lista:
        if (flag_altura == False):
            personaje_menor = personaje[primer_key]
            nom_personaje_menor = personaje['nombre']
            flag_altura = True

        elif (personaje[primer_key] < personaje_menor):
            personaje_menor = personaje[primer_key]
            nom_personaje_menor = personaje['nombre']
    menor=f"{personaje_menor}, {nom_personaje_menor}"
    return nom_personaje_menor, personaje_menor

def calcular_max_min_dato(lista:list, dato_a_realizar:str, key:str)->str:
    if dato_a_realizar=="maximo":
        max=calcular_max(lista, key)
        return max
    elif dato_a_realizar=="minimo":
        min=calcular_min(lista, key)
        return min
    else:
        print("Debe elegir entre 'maximo' o 'minimo' a calcular")

def stark_calcular_imprimir_heroe(lista:list, dato_a_realizar:str, key:str)->str:
    if len(lista)>0:
        retorno=calcular_max_min_dato(lista, dato_a_realizar, key)
        imprimir_dato(retorno)
    else:
        return -1
    

#              opcion 5                 #
def sumar_dato_heroe(lista:list, key:str)->int:
    dato2=0
    for heroe in lista:
        if type(heroe)==dict:
            dato=heroe[key]
            dato2+=dato
    return dato2

def dividir(dividendo:int, divisor:int)->float:  
    if divisor == 0:
        return 0
    else: 
        division=dividendo/divisor
        return division


def calcular_promedio(lista: list, key: str) -> float:
    contador=0
    acumulador=sumar_dato_heroe(lista, key)
    for personaje in lista:
        contador += 1
    promedio=dividir(acumulador, contador)
    return promedio

def stark_calcular_imprimir_promedio_altura(lista:list)->None:
    if len(lista)>0:
        promedio=calcular_promedio(lista, "altura")
        imprimir_dato(promedio)
    else:
        return -1



#              MENU                 #
def imprimir_menu()->None:
    dato="""
                ****MENU DE OPCIONES****

***tener en cuenta que antes de poder ver cualquiera de los datos, primero debe cargar y normalizar datos***

0. Cargar lista y normalizar datos
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
6. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
7. Calcular e informar cual es el superhéroe más y menos pesado.
8. Salir.

"""
    imprimir_dato(dato)

def validar_entero(numero:str)->bool:
    if numero.isdigit():
        return True
    else:
        return False
    
def stark_menu_principal():
    imprimir_menu()
    opcion=input("ingrese opcion: ")
    if validar_entero(opcion):
        opcion=int(opcion)
        return opcion
    else:
        return -1
    

def stark_marvel_app(lista:list)->None:
    flag_01=False
    flag_02=False

    while True:
        os.system("cls")

        opcion=stark_menu_principal()

        if opcion == 0:

            opcion2=print("""Bienvenido, elija alguna de las siguientes opciones antes de avanzar:
            1- cargar datos
            2-normalizar datos
            """)
            opcion2=int(input("ingrese opcion:"))

            if opcion2==1:
                lista=[]
                nueva_lista(lista_personajes, lista)
                print("datos cargados")
                flag_01=True

            if opcion2==2:
                if flag_01==True:
                    stark_normalizar_datos(lista, "altura", float)
                    stark_normalizar_datos(lista, "peso", float)
                    stark_normalizar_datos(lista, "fuerza", int)
                    print("Datos normalizados.")
                    flag_02=True
                else:
                    print("Lista de heroes vacia.")

        elif opcion == 1:
                if flag_01==True:
                    stark_imprimir_nombres_heroes(lista)
                else:
                    print("Primero normaliza datos (opcion 0)")
        elif opcion == 2:
            if flag_02==True:
                stark_imprimir_nombres_alturas(lista)
            else:
                print("Primero normaliza datos (opcion 0)")
        elif opcion == 3:
            if flag_02==True:
                stark_calcular_imprimir_heroe(lista, "maximo", "altura")
            else:
                print("Primero normaliza datos (opcion 0).")
        elif opcion == 4:
            if flag_02==True:
                stark_calcular_imprimir_heroe(lista, "minimo", "altura")
            else:
                print("Primero normaliza datos (opcion 0)")
        elif opcion == 5:
            if flag_02==True:
                stark_calcular_imprimir_promedio_altura(lista)
            else:
                print("Primero normaliza datos (opcion 0)")
        elif opcion == 6:
            if flag_02==True:
                stark_calcular_imprimir_heroe(lista, "maximo", "altura")
                stark_calcular_imprimir_heroe(lista, "minimo", "altura")
            else:
                print("Primero normaliza datos (opcion 0)")
        elif opcion == 7:
            if flag_02==True:
                stark_calcular_imprimir_heroe(lista, "maximo", "peso")
                stark_calcular_imprimir_heroe(lista, "minimo", "peso")
            else:
                print("Primero normaliza datos (opcion 0)")
        elif opcion == 8:
            break
        os.system("pause")
