from no1_extract_from_excel import extract_data
from korean_encoding import korean_font_config
korean_font_config()
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns



if __name__ == "__main__":
    df = extract_data()
    # print(df.keys())
    # exit()
    # print(df.keys())
    # exit()
    sales_by_year = df.groupby('년도')['판매금액'].sum().reset_index()

    # plt.figure(figsize=(10,10))
    # sns.barplot(
    #     data=sales_by_year,
    #     x="년도",
    #     y='판매금액'
    # )
    # plt.title("연도별 매출액", fontsize=30)
    # plt.show()

    #**데이터 요약(Aggregation)**
    revenue_profit_by_year = df.groupby("연령대").agg(
        평균판매금액 = ("판매금액", "mean"),
        평균순이익 = ("순이익", "mean"),
        순이익분산 = ('순이익', "std")
    ).reset_index()

    plot_df = revenue_profit_by_year.melt(
        id_vars='연령대',
        value_vars=["평균판매금액", "평균순이익", "순이익분산"],
        var_name = "구분",
        value_name = "금액"
    )

    plt.figure(figsize=(10,10))
    sns.barplot(
        data=plot_df,
        x="금액",
        y="연령대",
        hue="구분"
    )
    plt.title("연령대별 매출금액 및 순이익")
    plt.show()

    sales_by_gender_year = df.pivot_table (
        index="년도",
        columns="성별",
        values="판매금액",
        aggfunc="sum"
       ).reset_index()

plt.figure(figsize=(10,8))
sns.heatmap(
    sales_by_gender_year,
    cmap="YlGnBu",  # 오타 수정 완료
    annot=True,
    fmt=".0f"
)
plt.title("연도별/성별 매출 합계 히트맵")
plt.show()