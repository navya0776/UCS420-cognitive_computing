import pandas as pd

data = {
    "Td": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)

print(df.iloc[[0, 4, 7, 8]])

print(df.iloc[3:8])

print(df.iloc[4:9, 2:5])

print(df.iloc[:, 1:4])

import pandas as pd

iris_df = pd.read_csv("Iris.csv")

print(iris_df.head())

iris_df = iris_df.drop(iris_df.index[3])

iris_df = iris_df.drop(iris_df.columns[2] ,axis =1 )

print(iris_df)

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15",
        "2017-07-19",
        "2013-06-01",
        "2021-02-10",
        "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

employees = pd.DataFrame(data)

print(employees)
print(employees.shape)
print(employees.info())
print(employees.dtypes)
print(employees.describe())
print(employees.head(5))
print(employees.tail(3))
average_salary = employees["Salary"].mean()
print("Average Salary:", average_salary)
total_bonus = employees["Bonus"].sum()
print("Total Bonus:", total_bonus)
youngest_age = employees["Age"].min()
print("Youngest Age:", youngest_age)
highest_rating = employees["Rating"].max()
print("Highest Rating:", highest_rating)
employees = employees.sort_values(by="Salary", ascending=False)
print(employees)
def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

employees["Performance"] = employees["Rating"].apply(performance_category)
print(employees)
print(employees.isnull().sum())
employees = employees.rename(columns={"Employee_ID": "ID"})
print(employees)
more_experience = employees[employees["Years_of_Experience"] > 5]
print(more_experience)
it_employees = employees[employees["Department"] == "IT"]
print(it_employees)
employees["Tax"] = employees["Salary"] * 0.10
print(employees)
employees.to_csv("employees_modified.csv", index=False)
print("File saved successfully.")