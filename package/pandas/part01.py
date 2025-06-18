import pandas as pd 

df = pd.read_csv("./students.csv")

print('*'*30,'顯示前面五項','*'*30)
print(df.head())
print('*'*30,'name與math','*'*30)
print(df[['name','math']])
print('*'*30,'數學高於80分','*'*30)
print(df[df['math']>80])
print('*'*30,'所有女生的英文成績','*'*30)
print(df[df['gender']=="F"][['name','english']])
print('*'*30,'年齡大於16且自然科學成績大於90','*'*30)
result = df[(df['age'] >= 16 ) & (df['science'] > 90)]
print(result)
