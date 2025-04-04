# Escritura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo escritura ('w')
archivo = open('my_notes.txt', 'w')

# Escribimos al menos tres líneas de notas personales en el archivo
archivo.write("Mi nombre es Charlie Marcia Palacios, Tengo 33 años.\n")
archivo.write("Soy Militar, trabajo en la Fuerza Aerea Ecuatoriana en la ciudad de Guayaquil.\n")
archivo.write("Tengo una hermosa familia a la cual amo mucho mis 4 hijos y mi esposa.\n")

# Luego cerramos el archivo
archivo.close()

# Se abre el archivo 'my_notes.txt' en modo lectura ('r')
archivo = open('my_notes.txt', 'r')

# Leemos el contenido del archivo línea por línea y lo mostramos en pantalla
print(archivo.readline().strip())
print(archivo.readline().strip())
print(archivo.readline().strip())

# Cerrar el archivo después de leer
archivo.close()
