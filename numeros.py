# Importacion de la biblioteca Pillow para crear y manipular imágenes y biblioteca os para manejar rutas de archivos y directorios.
import os
from PIL import Image, ImageDraw, ImageFont

import string

carpeta_salida = os.path.join("Imagenes", "Numeros")
os.makedirs(carpeta_salida, exist_ok=True)

numbers = string.digits

for number in numbers:
    # aquí adentro, todo indentado, va tu lógica actual
    # pero usando "number" en vez de "1"
    print(f"Creando imagen_{number}.png")

    n = 15
    # Creacion de un lienzo para generar la imagen

    # n = Numero de pixeles de la imagen.
    # L, genera la imagen en escala de grises.

    image = Image.new('L', (n, n), color=255)

    # Obtener la fuente y el tamaño del texto
    font = ImageFont.truetype("fuente\Handlee-Regular.ttf", size=n)

    # Crear un objeto ImageDraw para dibujar en la imagen
    imageDrawer = ImageDraw.Draw(image)

    # Obtener el tamaño del texto para centrarlo en la imagen
    boxSize = imageDrawer.textbbox((0, 0), number, font=font)

    ancho_texto = boxSize[2] - boxSize[0]
    alto_texto = boxSize[3] - boxSize[1]

    # Calcular la posición para centrar el texto
    x = (n - ancho_texto) // 2 - boxSize[0]
    y = (n - alto_texto) // 2 - boxSize[1]

    # Dibujar el número "1" en la imagen
    imageDrawer.text((x, y), number, font=font, fill=0)

    nombre_archivo = f"imagen_{number}.png"
    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)

    image.save(ruta_completa)


carpeta_salida_letras = os.path.join("Imagenes", "Letras")
os.makedirs(carpeta_salida_letras, exist_ok=True)

letters = string.ascii_lowercase #+ string.ascii_uppercase

for letter in letters:
    # aquí adentro, todo indentado, va tu lógica actual
    # pero usando "letter" en vez de "A"
    print(f"Creando imagen_{letter}.png")

    n = 15
    # Creacion de un lienzo para generar la imagen

    # n = Numero de pixeles de la imagen.
    # L, genera la imagen en escala de grises.

    image = Image.new('L', (n, n), color=255)

    # Obtener la fuente y el tamaño del texto
    font = ImageFont.truetype("fuente\Handlee-Regular.ttf", size=n)

    # Crear un objeto ImageDraw para dibujar en la imagen
    imageDrawer = ImageDraw.Draw(image)

    # Obtener el tamaño del texto para centrarlo en la imagen
    boxSize = imageDrawer.textbbox((0, 0), letter, font=font)

    ancho_texto = boxSize[2] - boxSize[0]
    alto_texto = boxSize[3] - boxSize[1]

    # Calcular la posición para centrar el texto
    x = (n - ancho_texto) // 2 - boxSize[0]
    y = (n - alto_texto) // 2 - boxSize[1]

    # Dibujar la letra "A" en la imagen
    imageDrawer.text((x, y), letter, font=font, fill=0)

    nombre_archivo = f"imagen_{letter}.png"
    ruta_completa = os.path.join(carpeta_salida_letras, nombre_archivo)

    image.save(ruta_completa)