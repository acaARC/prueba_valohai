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

# Crear una imagen grande y bonita
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
ax.text(0.5, 0.5, f"{number_1} + {number_2} = {result}",
        fontsize=24, fontweight='bold', ha='center', va='center')
ax.set_facecolor('#f0f0f0')  # Fondo gris claro
ax.axis('off')  # Quitar ejes

# Guardar imagen
output_image = os.path.join(output_dir, 'sum_result.png')
fig.savefig(output_image, bbox_inches='tight')
plt.close(fig)

# Guardar un pequeño txt para control
control_txt = os.path.join(output_dir, 'finished.txt')
with open(control_txt, 'w') as f:
    f.write('Script finalizado correctamente.\n')

print(f"Imagen y control guardados en {output_dir}")
