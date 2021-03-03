import pandas as pd

df = pd.read_csv("data/Data_Job_WA.csv")

print(df.head())
#print(df.describe())

# Print median salary for "data scientist" positions in WA state
print("Median Min_Salary: ", df["Min_Salary"].median())
print("Median Max_Salary: ", df["Max_Salary"].median())