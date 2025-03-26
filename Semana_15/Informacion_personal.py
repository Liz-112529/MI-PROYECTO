# Crear un diccionario con información de una persona (ficticia)
informacion_personal = {
    "nombre": "Charlie Marcia",
    "edad": 33,
    "ciudad": "Latacunga",
    "profesion": "Militar"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992926333"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final en pantalla
print("Diccionario final:",informacion_personal)