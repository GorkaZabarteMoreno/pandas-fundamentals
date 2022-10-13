import pandas as pd

if __name__ == '__main__':
    names = ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
             'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
             'Jakeem', 'Helena', 'Ismat', 'Anila', 'Skye', 'Daniel', 'Aisha']
    grades = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]
    hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5, 13.75, 9.0, 8.0, 15.5,
             8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]
    data = pd.DataFrame({'Name': names, 'StudyHours': hours, 'Grade': grades})

    row0to5 = data.loc[0:5]  # Access data based on label or boolean array of the same lenght
    row0to6 = data.iloc[0:6]  # Access data based on index / data.iloc[start:stop], it does not include the stop index
    # Access data on range(0,6) which does not include the number 6

    row0columns1and2 = data.iloc[0, [1, 2]]
    row0columnGrade = data.loc[0, "Grade"]

    rowAisha0 = data.loc[data["Name"] == "Aisha"]
    rowAisha1 = data[data["Name"] == "Aisha"]
    rowAisha2 = data.query('Name=="Aisha"')
    print(rowAisha0, "\n",  rowAisha1, "\n", rowAisha2)  # A lot of different ways to perform the same

    name0 = data.Name  # Refer to a column as a property
    name1 = data["Name"]  # Refer to a column as an index value
