# SERIES EXAMPLE

# import pandas as pd #As 'pd' so you don't have to type 'pandas' every time
# colors = ['orange','white','blue','green',] #square brackets = list

# print(type(colors))

# color_series = pd.Series(colors) #

# print(type(color_series))
# print(color_series)

#SERIES DICTIONARY EXAMPLE

# students = {'Kansas':'Yvan','New Mexico':'Jon','Tennessee':'Andrew'}
# print(type(students))
# print(students.keys)
# print(students.values)

# student_series = pd.Series(data=students.values(),index=students.keys())
# print('\n')
# print(student_series)

#INDEX IN PANDAS


#DATAFRAMES IN PANDAS

# print('\n')
# filename = 'big-mac-full-index.csv'
# df = pd.read_csv(filename)

# print(df)

#CREATING A QUERY

import pandas as pd

filename = 'big-mac-full-index.csv'

df = pd.read_csv(filename)

query_1 = f"(iso_a3 == 'ARG)"
df_argentina = df.query(query_1)

print(df_argentina)

df_argentina.to_csv('argentina_report.csv')
