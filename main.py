"""
main file of the project
"""
import pandas as pd


if __name__ == '__main__':
    app_name: str = 'Gorka'
    print(f'{app_name} application')

    data = pd.read_csv(filepath_or_buffer="./data/grades.csv", delimiter=",", header="infer")
    print(data.head())
