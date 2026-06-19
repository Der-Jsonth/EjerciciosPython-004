codigos = [200,100,300,500]

def verificar_codigo(codigo):
    codigo is int
    if codigo in codigos:
        return True
    else:
        return False

def buscar_codigo():
    codigo = int(input("Entrege un codigo"))
    if verificar_codigo(codigo) == True:
        print("Existe dentro de la lista")
    else:
        print("no existe")
    return

buscar_codigo()