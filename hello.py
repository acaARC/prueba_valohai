import valohai
import pandas as pd
import numpy as np

my_inputs = {
    'dataset': 's3://valohai-academy-files/tutorials/valohai101/*.csv'
}

valohai.prepare(
    step="hello-job",
    default_inputs=my_inputs
)

print("Hello Valohai")

# Leer e imprimir las primeras filas de cada dataset
for file in valohai.inputs('dataset').paths():
    print(f"\n=== Leyendo archivo: {file} ===")
    df = pd.read_csv(file)
    print(df.iloc[:5, :3])

# Crear y guardar un CSV con datos aleatorios
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
df.to_csv(valohai.outputs().path('mydatafile.csv'), index=False)
print("\nArchivo aleatorio guardado como: mydatafile.csv")
