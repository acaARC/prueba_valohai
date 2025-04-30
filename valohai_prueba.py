import valohai

# Crear una imagen con colores random para simular salida de un proceso
from PIL import Image
import random
import shutil

valohai.prepare(step="playing-with-outputs")

width, height = 256, 256 # Dimensiones de la imagen
img = Image.new('RGB', (width, height)) # Crear una nueva imagen RGB
pixels = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(width * height)
] # Asignar a cada píxel un color aleatorio
img.putdata(pixels) # Colocar los píxeles en la imagen
output_filename = 'imagen_colores_random.png'
img.save(output_filename)

# Definir la ruta de salida en Valohai
output_path= valohai.outputs().path('mi_ejemplo_output.png')
shutil.copy(output_filename, output_path) # Copiar la imagen al directorio de salida