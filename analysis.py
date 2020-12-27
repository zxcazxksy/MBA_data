import pandas as pd

df = pd.read_csv('raw_data.csv')

means_total = df["Salary"].groupby([df["Race"], df["Gender"], df["Ed"]]).mean()

means_ed = df["Salary"].groupby([df["Gender"], df["Ed"]]).mean()

means_race = df["Salary"].groupby([df["Race"],df["Gender"]]).mean()

print(means_race)