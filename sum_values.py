import os

# Obtener los parámetros de entrada
number_1 = int(os.getenv('VH_PARAMETER_number_1', 0))
number_2 = int(os.getenv('VH_PARAMETER_number_2', 0))

# Sumar los números
sum_result = number_1 + number_2

# Ruta de salida
output_file = os.getenv('VH_OUTPUTS_DIR', '.') + "/result.txt"

# Guardar el resultado en un archivo
with open(output_file, 'w') as f:
    f.write(f"The sum of {number_1} and {number_2} is {sum_result}\n")

print(f"Sum result saved to: {output_file}")
