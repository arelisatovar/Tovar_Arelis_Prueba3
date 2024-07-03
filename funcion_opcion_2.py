def grabar_auto (buscar_auto, grabar):
    if len(buscar_auto) == 0:
                print("No hay informacion en la lista")        
    else:  
        print(f'{grabar["Tipo"]}\n{grabar["patente"]}\n{grabar["marca"]}\n{grabar["precio"]}\n{grabar["multa"]}\n')
    return           