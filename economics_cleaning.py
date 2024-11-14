import pandas as pd 

bank = pd.read_csv('bank_marketing.csv')

economics = bank.loc[:,['client_id','cons_price_idx','euribor_three_months']]

print(economics.sample(15))
print(economics.info())

economics.to_csv('economics.csv',index = False)