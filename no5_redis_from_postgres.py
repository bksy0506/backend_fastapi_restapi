# from sqlalchemy import create_engine
# import pandas as pd
# import redis
# import json
#
#
#
# # DB 연결 설정
# engine = create_engine(
#     "postgresql+psycopg2://soo:1234@localhost:5432/mydb"
#
# )
# redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
#
# # 이 부분 앞에 있는 공백을 모두 지우세요!
# df = pd.read_sql("select * from sales_information", con=engine)
# print(df.keys())
# sales_by_year = df.groupby(["product_name").agg(
#     revenue=("revenue", "sum"),
#     profit=("profit", "sum")
#
# ).reset_index()
#
# key = "dashboard:sales:product"
#
#
# for _, row in sales_by_product.iterrows():
#     redis_client.hset(
#         redis_table,
#         row["product_name"],
#         json.dumps(
#             {
#                 "revenue": int(row["revenue"]),
#                 "profit": int(row["profit"])
#             }
#         )
#     )
#
# result = redis_client.hgetall(redis_table)
# pivot_df= pd.DataFrame.from_dict(
#     {k:json.loads(v) for k,v in result.items()},
#     orient='index',).reset_index().rename(columns={'index':'product_name'})
#  print(pivot_df)