# Importación de librerías
import random

# Definición del abecedario
abecedario = 'abcdefghijklmnopqrstuvwxyz'

def encriptar(mensaje, clave):
    """
    Función que encripta un mensaje utilizando una clave para desplazar las letras en el abecedario.
    """
    encriptado = ''
    for letra in mensaje:
        # Verificar si la letra está en el abecedario
        if letra.lower() in abecedario:
            # Obtener el índice de la letra en el abecedario y aplicar el desplazamiento
            indice = (abecedario.index(letra.lower()) + clave) % len(abecedario)
            # Agregar la letra encriptada al mensaje encriptado
            encriptado += abecedario[indice]
        else:
            # Si la letra no está en el abecedario, agregarla tal cual al mensaje encriptado
            encriptado += letra
    return encriptado

def desencriptar(mensaje, clave):
    """
    Función que desencripta un mensaje encriptado utilizando una clave para desplazar las letras en el abecedario.
    """
    desencriptado = ''
    for letra in mensaje:
        # Verificar si la letra está en el abecedario
        if letra.lower() in abecedario:
            # Obtener el índice de la letra en el abecedario y aplicar el desplazamiento inverso
            indice = (abecedario.index(letra.lower()) - clave) % len(abecedario)
            # Agregar la letra desencriptada al mensaje desencriptado
            desencriptado += abecedario[indice]
        else:
            # Si la letra no está en el abecedario, agregarla tal cual al mensaje desencriptado
            desencriptado += letra
    return desencriptado

# Obtener el mensaje del usuario
mensaje = input("Ingrese el mensaje: ")
# Generar una clave aleatoria para la encriptación
clave = random.randint(1, len(abecedario)-1)

# Encriptar el mensaje
mensaje_encriptado = encriptar(mensaje, clave)
print("Mensaje encriptado:", mensaje_encriptado)

# Desencriptar el mensaje encriptado utilizando la misma clave
mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)
print("Mensaje desencriptado:", mensaje_desencriptado)






