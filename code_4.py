import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code): #NEED TO SOLVE CASE SENSITIVITY ISSUE
    df = pd.read_csv('./big-mac-full-index.csv')
    query1 = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
    query1_result = df.query(query1)
    mean_dollar_price2dec = round(query1_result['dollar_price'].mean(),2)
    return mean_dollar_price2dec

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    query2 = f"(iso_a3 == '{country_code.upper()}')"
    query2_result = df.query(query2)
    mean_price_overall2dec = round(query2_result['dollar_price'].mean(),2)
    return mean_price_overall2dec

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query3 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    query3_result = df.query(query3)
    cheapest_price_index = query3_result['dollar_price'].idxmin()
    target_row = query3_result.loc[cheapest_price_index]
    country_name = target_row.iloc[3]
    country_code = target_row.iloc[1]
    dollar_price = round(target_row.iloc[6],2)
    return f"{country_name}({country_code}): ${dollar_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query4 = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    query4_result = df.query(query4)
    maximum_price_index = query4_result['dollar_price'].idxmax()
    target_row = query4_result.loc[maximum_price_index]
    country_name = target_row.iloc[3]
    country_code = target_row.iloc[1]
    dollar_price = round(target_row.iloc[6],2)
    return f"{country_name}({country_code}): ${dollar_price}"


if __name__ == "__main__":
    result_1 = get_big_mac_price_by_year(2010,'arg')
    print(result_1)

    result_2 = get_big_mac_price_by_country('mex')
    print(result_2)

    result_3 = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_3)

    result_4 = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_4)


