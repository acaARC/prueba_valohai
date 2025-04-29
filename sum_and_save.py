import valohai
import os
import matplotlib.pyplot as plt

# Preparar valohai
valohai.prepare(step='Sum two numbers')

# Leer parámetros
number_1 = valohai.parameters('number_1').value
number_2 = valohai.parameters('number_2').value

# Hacer la suma
result = number_1 + number_2
print(f"La suma es: {result}")

# Crear carpeta de output
output_dir = valohai.outputs('result').path('sum_output')
os.makedirs(output_dir, exist_ok=True)

# Crear una imagen mostrando el resultado
fig, ax = plt.subplots(figsize=(6, 3))
ax.text(0.5, 0.5, f"{number_1} + {number_2} = {result}",
        fontsize=20, ha='center', va='center')
ax.axis('off')  # Ocultar ejes

# Guardar imagen
output_image = os.path.join(output_dir, 'sum_result.png')
fig.savefig(output_image)
plt.close(fig)

print(f"Imagen del resultado guardada en {output_image}")
