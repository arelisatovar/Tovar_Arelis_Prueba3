def imprimir_certificado(valor_multas, valor_an, valor_em, buscar_auto,):
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
    return 