import valohai
import os

# Preparar valohai
valohai.prepare(step='Sum two numbers')

# Leer parámetros
number_1 = valohai.parameters('number_1').value
number_2 = valohai.parameters('number_2').value

# Hacer la suma
result = number_1 + number_2
print(f"La suma es: {result}")

# Guardar resultado en /valohai/outputs
output_path = valohai.outputs('result').path('sum.txt')
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w') as f:
    f.write(f"La suma de {number_1} + {number_2} es {result}\n")

print(f"Resultado guardado en {output_path}")
