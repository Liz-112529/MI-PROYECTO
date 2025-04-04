# Escritura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos al menos tres líneas de notas personales en el archivo
    file.write("Mi nombre es Charlie Marcia Palacios, Tengo 33 años.\n")
    file.write("Soy Militar, trabajo en la Fuerza Aerea Ecuatoriana en la ciudad de Guayaquil.\n")
    file.write("Tengo una hermosa familia a la cual amo mucho mis 4 hijos y mi esposa.\n")

# Lectura de texto con readline()
# Abrimos el archivo en modo "r" para leer el contenido
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea utilizando readline()
    line = file.readline()  # Permite leer la primera línea
    while line:
        print(line.strip())  # Imprime la línea sin saltos
        line = file.readline()  # Lee la siguiente línea

# El archivo se cierra automáticamente al salir del bloque with
