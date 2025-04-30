import valohai
import pandas as pd

valohai.prepare(step="hello-job")

print("Hello Valohai")

# Iterar sobre todos los archivos descargados
for file in valohai.inputs('dataset').paths():
    print(f"Procesando archivo: {file}")
    df = pd.read_csv(file)
    print(df.iloc[:5, :3])
