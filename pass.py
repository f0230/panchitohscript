import random
import string

longitud = int(input("Ingrese la longitud de la contraseña (entre 16 y 24 caracteres): "))

def generar_contraseña_segura(longitud):
    if longitud < 16 or longitud > 24:
        raise ValueError("La longitud de la contraseña debe estar entre 16 y 24 caracteres.")
    
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    caracteres_especiales = string.punctuation

    todos_caracteres = minusculas + mayusculas + numeros + caracteres_especiales
    random_gen = random.SystemRandom()


    while True:
        contraseña = ''.join(random_gen.choices(todos_caracteres, k=longitud))
        if (set(contraseña) & set(minusculas) and
            set(contraseña) & set(mayusculas) and
            set(contraseña) & set(numeros) and
            set(contraseña) & set(caracteres_especiales)):
            return contraseña

try:
    contraseña_segura = generar_contraseña_segura(longitud)
    print(f"Tu nueva contraseña es: {contraseña_segura}")
except ValueError as e:
    print(e)
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (entre 16 y 24 caracteres): "))
            contraseña_segura = generar_contraseña_segura(longitud)
            print(f"Tu nueva contraseña es: {contraseña_segura}")
            break
        except ValueError as e:
            print(e)