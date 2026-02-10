import pandas as pd


def extract_data():
    df = pd.read_excel("./data/Details.xlsx", sheet_name=None)
    region = df['지역']
    promotion = df["프로모션"]
    channel = df["채널"]
    date = df["날짜"]
    customer = df["2018년도~2022년도 주문고객"]
    product = df["제품"]
    category = df["분류"]
    product_category = df["제품분류"]
    sales = pd.read_excel("./data/Sales.xlsx", sheet_name="Sheet1")
    # print(sales.keys())
    # exit()
    merged_all = (
        sales
        .merge(date, on='날짜', how='left')
        .merge(product, on="제품코드", how='left')
        .merge(customer, on="고객코드", how='left')
        .merge(promotion, on="프로모션코드", how='left')
        .merge(channel, on='채널코드', how='left')
        .merge(product_category, on='제품분류코드', how='left')
        .merge(category, on='분류코드', how='left')
        .merge(region, on='지역코드', how='left')
    )[['날짜', '제품코드', '고객코드', '프로모션코드', '채널코드', 'Quantity', '지역_x',
       '날짜코드', '년도', '분기', '월(No)', '월(영문)', '제품명', '색상', '원가', '단가', '제품분류코드',
       '지역코드', '고객명', '성별', '생년월일', '프로모션', '할인율', '채널명', '제품분류명', '분류코드',
       '분류명', '시도', '구군시']]
    merged_all.rename({"Quantity": "수량", "지역_x": " 지역"}, axis=1, inplace=True)
    merged_all["판매금액"] = merged_all["단가"] * (1 - merged_all['할인율']) * merged_all['수량']
    merged_all["순이익"] = ((merged_all["단가"] * (1 - merged_all['할인율'])) - merged_all['원가']) * merged_all['수량']
    merged_all["나이"] = (merged_all["날짜"].dt.year - merged_all['생년월일'].dt.year).round().astype(int)
    merged_all["연령대"] = pd.cut(
        merged_all['나이'],
        bins=[0, 19, 29, 39, 49, 59, 69, 200],
        labels=["--20", "20대", "30대", "40대", "50대", "60대", "60++"],
    )
    return merged_all


if __name__ == "__main__":

    merged_all = extract_data()
    print(merged_all)