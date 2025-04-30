import valohai
import pandas as pd

# Preparar inputs
my_inputs = {
    'dataset': [
        's3://valohai-academy-files/tutorials/valohai101/2020.csv',
        's3://valohai-academy-files/tutorials/valohai101/2021.csv',
        's3://valohai-academy-files/tutorials/valohai101/2022.csv',
    ]
}

valohai.prepare(
    step="hello-job",
    default_inputs=my_inputs
)

print("Hello Valohai\n")

dataframes = []

for file in valohai.inputs('dataset').paths():
    print(f"=== Leyendo archivo: {file} ===")
    df = pd.read_csv(file)
    print(df.head(), "\n")
    dataframes.append(df)

# Guardar dataset combinado
combined_df = pd.concat(dataframes, ignore_index=True)
output_path = valohai.outputs().path('combined.csv')
combined_df.to_csv(output_path, index=False)
print(f"Archivo combinado guardado en: {output_path}")
