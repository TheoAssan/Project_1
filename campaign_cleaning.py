import pandas as pd 

bank = pd.read_csv('bank_marketing.csv')

campaign = bank.loc[:,['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']]

# converting the required columns to boolean data type 
campaign['previous_outcome'] = campaign['previous_outcome'].str.lower()
campaign['previous_outcome'] = campaign['previous_outcome'].replace({'nonexistent':False,'failure':False,'success':True})

campaign['campaign_outcome'] = campaign['campaign_outcome'].str.lower()
campaign['campaign_outcome'] = campaign['campaign_outcome'].replace({'no':False,'yes':True})

# creating the last_contact_date column
bank['month'] = pd.to_datetime(bank['month'],format='%b').dt.month

campaign['last_contact_date'] = pd.to_datetime({'year':2022,'month':bank['month'],'day':bank['day']})

print(campaign.head(15))

campaign.to_csv('campaign.csv',index = False)
