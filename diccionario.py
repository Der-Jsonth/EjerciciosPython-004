lista = ["Jesús", 2, True] # -> indice: 0

lista[0]

diccionario = {
    "nombre": "Jesús",
    "edad": 34,
    "ramos": ["Fundamentos", "FS1", "FS2", "FS3"],
    "carrera": {
        "titulo": "Ing. informatica",
        "anio": 2012
    }
}

# Acceder a los elementos del diccionario
diccionario["nombre"]
diccionario["ramos"][0]
diccionario["carrera"]["titulo"]

if diccionario.get("telefono") == None:
    print("el elemento no existe")

print(diccionario.get("telefono"))

# Agregar
diccionario["telefono"] = 123456789

if diccionario.get("telefono") == None:
    print("el elemento no existe")

print(diccionario.get("telefono"))

# Actualizar
diccionario["telefono"] = 23

print(diccionario.get("telefono"))

# Eliminar
del diccionario["telefono"]

print(diccionario.get("telefono"))