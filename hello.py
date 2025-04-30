import valohai
import pandas as pd

# Definir múltiples archivos como input por defecto
my_inputs = {
    'dataset': [
        's3://valohai-academy-files/tutorials/valohai101/2020.csv',
        's3://valohai-academy-files/tutorials/valohai101/2021.csv',
        's3://valohai-academy-files/tutorials/valohai101/2022.csv'
    ]
}

# Preparar ejecución
valohai.prepare(
    step="hello-job",
    default_inputs=my_inputs
)

print("=== Hello Valohai ===")
# Leer e imprimir los datasets
for i, file in enumerate(valohai.inputs('dataset').paths()):
    print(f"\n--- Dataset {i+1}: {file} ---")
    try:
        df = pd.read_csv(file)
        print(df.head(5))
    except Exception as e:
        print(f"Error al leer {file}: {e}")
