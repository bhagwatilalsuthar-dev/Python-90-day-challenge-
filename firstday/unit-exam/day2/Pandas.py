
import pandas as pd
A=pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(A)

#  Data={
#     "Department":["IT","HR","IT","HR"],
#     "Salary":[50000,40000,60000,45000]
# }
# import pandas as pd 
# df=pd.DataFrame(Data)
# print(df.groupby("Department")["Salary"].sum())

Data={
    "Name":["Aman","Sohan","Ramesh"],
    "Age":[25,30,15],
    "Marks":[50,60,70]
}
import pandas as pd
df=pd.DataFrame(Data)
# print(df)



##DataFrame pandas
Data={
    "Name":["Ram","Shyam","Mohan"],
	"Age":[25,30,28],
	"Salary":[30000,40000,35000]
}

# import pandas as pd
# df=pd.DataFrame(Data)
# ##original DataFrame 
# print("Original Dataframe")
# print(df)
# ##Filter DataFrame Salary>32000
# Filter_df=df[df["Salary"]>32000]
# print("\nSalary>32000")
# print(Filter_df)
# ##salary add Bonus+5000
# Bonus_df=df["bonus"]=df["Salary"]+5000
# print("\nBonus Add")
# print(Bonus_df)
# ##dastop pe Bonus dikhana 
# sorted_df = df.sort_values("Salary", ascending=False)
# print(sorted_df)

## TASK 2 (Thoda Realistic Data)
##Ek company me employees ka data hai:

Data={
    "Name":["Ram","Shyam","Mohan","Geeta","Shita"],
    "Department":["IT","HR","IT","Finance","HR"],
    "Salary":[50000,40000,60000,45000,42000],
    "Experience":[2,5,3,4,2]
}

import pandas as pd
df=pd.DataFrame(Data)
# print(df)
#Filter by IT department employees
Filter_df=df[df["Department"]=="IT"]
# print("\nFilter with It department")
# print(Filter_df)
##filter by salary >45000
salary_df=df[df["Salary"]>45000]
# print("\nSalary target se jada")
# print(salary_df)
##Experirnce filter 2 se jada
Experince_df=df[df["Experience"]>2]
# print("\nExperince 2 se jada")
# print(Experince_df)
##groupby average
group_df=df.groupby("Department")["Salary"].mean().astype(int)
# print(group_df)
## new colum
Bonus_df=df["Salary"]+ (df["Salary"] * 0.10)
# print("\n Salary add Bonus")
# print(Bonus_df)
## Highest salary wala employee nikalo
min_df=(df.loc[df["Salary"].idxmax()])
# print(min_df)


import pandas as pd
df=pd.read_csv("fast-day/unit-exam/day2/shalles_Data.csv")
# print(df)
head_df=df.head()
# print(head_df)
info_df=df.info()
# print(info_df)
statistics_df=df.describe().astype(int)
# print(statistics_df)
shape_df=df.shape[0],df.shape[1]
# print(shape_df)
d=df[['Name','Math']]
# print(d)
Average=df["Math"].mean()
# print("Average",Average)
# print(df[["Name","Science"]].max())
# print(df[df["Math"] >80][["Name","Math"]])
# print(df[df["Gender"]=="F"])
print(df[df["Attendance"]>90][["Name","Attendance"]])


