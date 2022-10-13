import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="../data/grades.csv")
    data = data.dropna(axis=0, how="any")
    data = data.sort_values(by="Grade", ascending=True)

    avg_hours = round(data.StudyHours.mean(), 3)
    avg_grades = round(data.Grade.mean(), 3)

    study_more = data[data.StudyHours > avg_hours]
    avg_grade_study_more = study_more.Grade.mean()

    passes = pd.Series(data.Grade >= 60)
    data = pd.concat([data, passes.rename("Pass")], axis=1)

    count_passes = data.groupby("Pass").Name.count()
    avg_group_pass = data.groupby("Pass")[["StudyHours", "Grade"]].mean()
