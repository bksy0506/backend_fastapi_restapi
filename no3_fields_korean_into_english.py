import pandas as pd
#여러 개의 시트(Sheet)를 한꺼번에 읽어와서, 각 시트의 한글 컬럼명을 미리 정해둔 영어 컬럼명으로 싹 바꿔버리는 자동화 작업
COLUMN_MAP = {
    #시트네임이 오브젝트로 되어있다.
    "날짜": {
        "날짜코드": "date_code",
        "날짜": "date",
        "년도": "year",
        "분기": "quarter",
        "월(No)": "month",
        "월(영문)": "month_name"
    },
    "제품": {
        "제품코드": "product_code",
        "제품명": "product_name",
        "색상": "color",
        "원가": "cost",
        "단가": "unit_price",

        "제품분류코드": "product_category_code"
    },
    "2018년도~2022년도 주문고객": {
        "고객코드": "customer_code",
        "고객명": "customer_name",
        "성별": "gender",
        "생년월일": "birth_date",
        "지역코드": "region_code"
    },
    "채널": {
        "채널코드": "channel_code",
        "채널명": "channel_name"
    },
    "프로모션": {
        "프로모션코드": "promotion_code",
        "프로모션": "promotion",
        "할인율": "discount_rate"
    },
    "지역": {
        "지역코드": "region_code",
        "시도": "sido",
        "구군시": "sigungu",
        "지역": "region"
    },
    "분류": {
        "분류코드": "category_code",
        "분류명": "category_name"
    },
    "제품분류": {
        "제품분류코드": "product_category_code",
        "제품분류명": "product_category_name",
        "분류코드": "category_code"
    }
}

if __name__ == "__main__":
     details = pd.read_excel("./data/Details.xlsx", sheet_name=None)

     converted_details = {
         sheet_name: table.rename(columns = COLUMN_MAP[sheet_name])
         for sheet_name, table in details.items() if sheet_name in COLUMN_MAP
     }
     output_details = "./data/details_en.xlsx"
     with pd.ExcelWriter(output_details) as writer:
         for sheet_name, table in converted_details.items():
             table.to_excel(writer, sheet_name = sheet_name, index = False)

    # sales = pd.read_excel("./data/Sales.xlsx")
    # columns = {
    #     "날짜": "sales_date",
    #     "제품코드": "product_code",
    #     "고객코드": "customer_code",
    #     "채널코드": "channel_code",
    #     "프로모션코드": "promotion_code",
    #     "Quantity": "quantity",
    #     "UnitPrice": "unit_price"
    # }
    # sales.rename(columns = columns, inplace = True)
    # sales.drop("지역", axis = 1, inplace = True)
    # print(sales.keys())
    #
    # output_sales = "./data/sales_en.xlsx"
    # sales.to_excel(output_sales, index = False)
