import valohai
import pandas as pd

my_inputs = {
    'dataset': [
        's3://valohai-academy-files/tutorials/valohai101/2020.csv',
        's3://valohai-academy-files/tutorials/valohai101/2021.csv',
        's3://valohai-academy-files/tutorials/valohai101/2022.csv'
    ]
}

valohai.prepare(
    step="hello-job",
    default_inputs=my_inputs
)

print("Hello Valohai")

for file in valohai.inputs('dataset').paths() :
    print(file)
    df = pd.read_csv(file)
    print(df.iloc[:5, :3])