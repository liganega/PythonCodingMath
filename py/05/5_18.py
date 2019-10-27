import pandas as pd

df = pd.read_csv('/파일 경로 직접 입력해 주세요/FIFA 2018 Statistics.csv')

print (df)
print (type(df))
print (df.columns)
print (df.columns[1])