create view sales_information as

select
    s.sales_date,
    s.quantity,
    s.unit_price,
    (s.quantity * s.unit_price * (1-pt.discount_rate)) as revenue,
    (s.quantity * (s.unit_price * (1-pt.discount_rate)-p.cost)) as profit,

    r.region_code,
    r.sido,
    r.sigungu,
    r.region,

    c.customer_code,
    c.customer_name,
    c.gender,
    c.birth_date,
    EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int AS age,
    case
        when EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int <20 then '--20'
        when EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int <30 then '20대'
        when EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int <40 then '30대'
        when EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int <50 then '40대'
        when EXTRACT(YEAR FROM age(s.sales_date, c.birth_date))::int <60 then '50대'
        else '60++'
end as age_group,

    p.product_code,
    p.product_name,
    p.color,
    p.price,

    ct.category_code,
    ct.category_name,

    pt.promotion_code,
    pt.promotion,
    pt.discount_rate,

    ch.channel_code,
    ch.channel_name

from sales s
join customer c
on s.customer_code = c.customer_code
join region r
    on c.region_code = r.region_code
join product p
on s.product_code = p.product_code
join product_category pc
on p.product_category_code = pc.product_category_code
join category ct
on pc.category_code = ct.category_code
join promotion pt
on s.promotion_code = pt.promotion_code
join channel ch
on s.channel_code = ch.channel_code
join date_dim dd
        on s.sales_date = dd.date


select * from sales_information;