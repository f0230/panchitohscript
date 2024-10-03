import random
import os
import string

# Listado básico de palabras para generar passphrases
palabras_comunes = [
    "Cafe", "Perro", "Sol", "Playa", "Rico", "Dulce", "Grande", 
    "Gato", "Viaje", "Mar", "Feliz", "Montaña", "Reloj", 
    # Añade más palabras según sea necesario
]

# Archivo donde almacenaremos las contraseñas generadas
archivo_contrasenas = "contrasenas_generadas.txt"

# Función para generar una passphrase
def generar_passphrase(num_palabras=4, longitud_numero=3):
    # Elegimos 'num_palabras' palabras aleatorias
    passphrase = ''.join(random.choice(palabras_comunes) for _ in range(num_palabras))
    
    # Generamos un número aleatorio con la longitud deseada
    numero_aleatorio = ''.join(random.choices(string.digits, k=longitud_numero))
    
    # Mezclamos la passphrase con el número
    passphrase += numero_aleatorio
    
    # Añadir caracteres especiales aleatorios
    passphrase += ''.join(random.choices(string.punctuation, k=2))  # Añadir 2 caracteres especiales aleatorios
    
    return passphrase

# Función para guardar contraseñas generadas
def guardar_contrasena(contrasena):
    with open(archivo_contrasenas, "a") as f:
        f.write(contrasena + "\n")

# Función para verificar si la contraseña ya existe
def es_unica(contrasena):
    if not os.path.exists(archivo_contrasenas):
        return True  # Si el archivo no existe, la contraseña es única
    with open(archivo_contrasenas, "r") as f:
        contrasenas_existentes = f.read().splitlines()
    return contrasena not in contrasenas_existentes

# Generador que solo devuelve contraseñas únicas
def generar_passphrase_unica(num_palabras=4, longitud_numero=3):
    while True:
        passphrase = generar_passphrase(num_palabras, longitud_numero)
        if es_unica(passphrase):
            guardar_contrasena(passphrase)
            return passphrase

# Ejemplo de uso
if __name__ == "__main__":
    # Genera una passphrase única
    passphrase = generar_passphrase_unica(num_palabras=6, longitud_numero=4)  # Permite 6 palabras y número de 4 dígitos
    print(f"Tu nueva passphrase es: {passphrase}")

