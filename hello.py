import valohai
import pandas as pd

valohai.prepare(step="hello-job")

print("Hello Valohai")

for file in valohai.inputs('dataset').paths():
    print(f"\n=== Leyendo archivo: {file} ===")
    df = pd.read_csv(file)
    print(df.head(5))
