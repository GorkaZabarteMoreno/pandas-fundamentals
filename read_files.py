import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv", delimiter=",", header="infer")
    print(data.head())
