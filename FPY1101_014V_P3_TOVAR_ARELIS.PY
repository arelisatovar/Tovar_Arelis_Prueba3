import os
from funciones import grabar_datos
from funcion_opcion_2 import grabar_auto
from funcion_opcion_3 import imprimir_certificado
from funcion_salir import salir_programa
os.system ("cls")

buscar_auto = []

# valores opcion 3
emision = 1
anotaciones = 2
multas = 3
valor_em = 1000
valor_an = 2000
valor_multas = 3000



while True:

    print("Bienvenido al menu")
    print("*" *(50))
    print("1.- Graba tus datos:")
    print("2.- Busca tus datos:")
    print("3.- Imprime el certificado que buscas:")
    print("4.- Salir del menu:")
    print("*" *(50))

    try:
        opcion = int(input("Ingresa una opcion: \n"))
    except:
        opcion = 0
    if opcion < 0 or opcion > 4:
        print("Error, ingrese una opcion valida:")     
    if opcion == 1:
            print("Graba los datos correspondientes al vehiculo:")
            grabar = grabar_datos()
            buscar_auto.append(grabar)         
    elif opcion == 2:
        print("Busca tus datos ingresados")
        auto = grabar_auto (buscar_auto, grabar)                  
    elif opcion == 3:
        print("Certificados")
        imprimir =  imprimir_certificado(valor_multas, valor_an, valor_em, buscar_auto)             
    else:
        salir = salir_programa()
        break
