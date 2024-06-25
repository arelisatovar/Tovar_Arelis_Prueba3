import os
from funciones import grabar_datos
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
            

    if opcion == 2:
            print("Buscar datos:")

            if len(buscar_auto) == 0:
                print("No hay informacion en la lista")
            
            else:
                print(f'{grabar["Tipo"]}\n{grabar["patente"]}\n{grabar["marca"]}\n{grabar["precio"]}\n{grabar["multa"]}\n')    
    
    if opcion == 3:
        for grabar in buscar_auto:
            print(grabar["patente"])
            print(grabar)
            
        print ("Imprime un certificado para la patente:")
        print("Tipos de certificados:")
        print("1.- Emision de contaminantes:")
        print("2.- Anotaciones vigentes:")
        print("3.- Multas:")
        
        certificado = input("Ingresa tu opcion:\n")
        if certificado == 1:
            print("El certificado de emision de contaminantes cuesta", valor_em)   
        elif certificado == 2:
            print("El certificado de anotaciones vigentes cuesta:", valor_an)
            
        elif certificado == 3:
            print("El certificado de multas, cuesta:", valor_multas)   
        else:
            print("No hay ningun certificado")
        
    if opcion == 4:
        print("Haz salido del programa:")
    
    break




