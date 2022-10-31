#ejercicio2
import pandas as pd
df=pd.read_csv("titanic.csv")
print(df[["Age","Sex","Embarked"]][df["Age"]>19])