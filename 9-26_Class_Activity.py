# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# query = f"(iso_a3 == 'NZL' or iso_a3 == 'DNK')"

# df_result = df.query(query)

# mean_dollar_price = df_result['dollar_price'].mean()

# mean_dollar_price_2decimal = mean_dollar_price

# print(df_result)
# print(mean_dollar_price)


#DIDNT FINISH EXAMPLE ABOVE (Comment everything above when using example below)


# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# print(df_result['dollar_price'].min())
# print(df_result['dollar_price'].max())
# print(df_result['dollar_price'].mean())
# print(df_result['dollar_price'].median())


# DATE QUERY EXAMPLE BELOW (FIXED ERROR)


import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')
year = '2000'
country_code = 'CHL'
query_2 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')" #YYYY-MM-DD 
query_3 = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')" #YYYY-MM-DD

df_date = df.query(query_2)
df_query3 = df.query(query_3)

print(df_query3)


#


# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# #the row with minimum $ price for big mac (Can be done with max as well)
# index_of_min_value = df['dollar_price'].idxmin() #returns an index (row)

# print(index_of_min_value) 

# print(df.loc[index_of_min_value]) #returns series as its the row (.loc = select data by label)


