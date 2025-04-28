import os
import valohai
import pandas as pd

# Preparar Valohai
valohai.prepare(
    step="train-in-out",
    default_parameters={"exponente": 2}
)

# Obtener parámetro
exponente = valohai.parameters('exponente').value
print(f"Exponente configurado: {exponente}")

# Obtener path del dataset
input_paths = list(valohai.inputs('dataset').paths())

if not input_paths:
    raise ValueError("No se ha proporcionado dataset.")

dataset_path = input_paths[0]

# Leer CSV
print(f"Leyendo dataset en: {dataset_path}")
df = pd.read_csv(dataset_path)

# Procesar: elevar cada valor a la potencia indicada
print("Procesando datos...")
processed_df = df.applymap(lambda x: x**exponente if isinstance(x, (int, float)) else x)

# Obtener output path
output_dir = valohai.outputs('result').path
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'processed_positions.csv')

# Guardar resultado
processed_df.to_csv(output_file, index=False)
print(f"Archivo procesado guardado en: {output_file}")
