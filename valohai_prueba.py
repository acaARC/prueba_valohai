import valohai

# Crear una imagen con colores random para simular salida de un proceso
from PIL import Image
import random
import shutil
import os

valohai.prepare(step="playing-with-outputs")

carpeta_cualquiera = 'carpeta_cualquiera' # Nombre de la carpeta donde se guardará la imagen

os.makedirs(carpeta_cualquiera, exist_ok=True) # Crear la carpeta si no existe

width, height = 256, 256 # Dimensiones de la imagen
img1 = Image.new('RGB', (width, height)) # Crear una nueva imagen RGB
pixels = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(width * height)
] # Asignar a cada píxel un color aleatorio
img1.putdata(pixels) # Colocar los píxeles en la imagen
output_filename = f'{carpeta_cualquiera}/imagen1_colores_random.png'
img1.save(output_filename)

img2 = Image.new('RGB', (width, height)) # Crear una nueva imagen RGB
pixels = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(width * height)
] # Asignar a cada píxel un color aleatorio
img2.putdata(pixels) # Colocar los píxeles en la imagen
output_filename = f'{carpeta_cualquiera}/imagen2_colores_random.png'
img2.save(output_filename)

# Definir la ruta de salida en Valohai
output_path= valohai.outputs().path('mi_ejemplo_output_carpeta')
shutil.copytree(carpeta_cualquiera, output_path) # Copiar la imagen al directorio de salida