import valohai
import pandas as pd

my_inputs = {
    'dataset': 's3://valohai-academy-files/tutorials/valohai101/2022.csv'
}

valohai.prepare(
    step="hello-job",
    default_inputs=my_inputs
)

print("Hello Valohai")

df = pd.read_csv(valohai.inputs('dataset').path())
print(df.iloc[:5, :3])