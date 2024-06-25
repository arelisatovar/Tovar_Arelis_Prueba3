def grabar_datos ():
    val_tipo = ""
    while val_tipo == "":
            tipo = input("Ingresa tipo - Entre: Automovil - Camion - Camioneta - Moto\n")
            val_tipo = tipo.replace(" ", "")
            if val_tipo == "":
                print ("Ingresa un tipo correcto")
        #Patente
    val_patente = ""
    while val_patente == "":
        patente = input("Ingresa patente \n")
        val_patente = patente.replace(" ", "")
        if val_patente == "":
            print ("Ingresa una patente correcta")
    #Marca
    val_marca = ""
    while val_marca == "":
        marca = input("Ingresa marca \n")
        val_marca = marca.replace(" ", "")
        if val_marca == "":
            print ("Ingresa una marca correcta")
    #Precio (hacerlo con try)
    val_precio = ""
    while val_precio == "":
        precio = input("Ingresa precio \n")
        val_precio = precio.replace(" ", "")
        if val_precio == "":
            print ("Ingresa un precio")
    #Multa
    val_multa = ""
    while val_multa == "":
        multa = input("Ingresa multa \n")
        val_multa = multa.replace(" ", "")
        if val_multa == "":
            print ("Ingresa multa valida")
            
    grabar = {"Tipo": tipo,
            "patente": patente,
            "marca": marca,
            "precio": precio,
            "multa": multa
            }
    
    return grabar