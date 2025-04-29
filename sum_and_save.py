import valohai
import os
import shutil

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

# Guardar resultado dentro de esa carpeta
output_file = os.path.join(output_dir, 'sum.txt')
with open(output_file, 'w') as f:
    f.write(f"La suma de {number_1} + {number_2} es {result}\n")

print(f"Resultado guardado en {output_file}")
