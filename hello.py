import pandas as pd
url = 'https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog'
x = pd.read_csv(url)
s=x.describe()
print(s)
s.to_excel('test.xlsx')