import pandas as pd
import numpy as np

pd.set_option('future.no_silent_downcasting', True)

# Reading the csv file 
bank = pd.read_csv('bank_marketing.csv')

# Creating the client dataframe
client = bank.loc[:, 'client_id':'mortgage']

# Replacing '.' with '_' in the education and job column
client['education'] = client['education'].str.replace('.','_',regex=False)
client['education'] = client['education'].replace('unknown',np.NaN)
client['job'] = client['job'].str.replace('.','_',regex=False)

# converting the credit_default column to boolean data type 
client['credit_default']= client['credit_default'].str.lower()
client['credit_default'] = client['credit_default'].replace({'no':False,'yes':True,'unknown':False})
client['credit_default'] = client['credit_default'].astype(bool)

# converting the mortgage column to boolean data type 
client['mortgage']= client['mortgage'].str.lower()
client['mortgage'] = client['mortgage'].replace({'no':False,'yes':True,'unknown':False})
client['mortgage'] = client['mortgage'].astype(bool)

print(client.loc[:, 'client_id':'mortgage'].isnull().any(axis=1))

client.to_csv('client.csv',index = False)



