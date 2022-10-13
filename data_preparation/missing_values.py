import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="../data/grades.csv")
    number_nans = data.isna().sum()
    number_nulls = data.isnull().sum()

    number_notnans = data.notna().sum()

    missing_rows = data[data.isna().any(axis=1)]

    # Fill with mean
    data.StudyHours = data.StudyHours.fillna(data.StudyHours.mean().round(2))

    # Drop rows with missing values
    data = data.dropna(axis=0, how="any")