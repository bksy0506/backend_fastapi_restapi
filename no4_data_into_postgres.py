import pandas as pd
from sqlalchemy import create_engine

emgine = create_engine("postgresql+psycopg2://soo:1234@localhost:5432/mydb")

if __name__=="__main__":

    details =pd.read_excel("./data/details_en.xlsx", sheet_name = None)
    print(details.keys())

    #region=details['지역']
   # print(region)

   # exit()
   # region.to_sql('region', emgine, if_exists='append', index = False)
    df = pd.read_excel('./data/sales_en.xlsx', sheet_name='Sheet1')
    df.to_sql("sales", con = emgine,if_exists='append', index = False)
    print(df.head())