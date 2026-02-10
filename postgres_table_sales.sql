create table region(
                       region_code int primary key,
                       sido varchar(50),
                       sigungu varchar(50),
                       region varchar(50)
);
create table promotion(
                          promotion_code int primary key,
                          promotion varchar(50),
                          discount_rate numeric(5,2)
);
create table channel(
                        channel_code int primary key,
                        channel_name varchar(50)
);

create table date_dim(
                         date_code int primary key,
                         date date,
                         year int,
                         Quarter int,
                         month int,
                         month_name varchar(50)
);

create table category(
                         category_code int primary key,
                         category_name varchar(100)
);

create table product_category(
                                 product_category_code varchar(10) primary key,
                                 product_category_name varchar(100),
                                 category_code int not null,
                                 constraint fk_product_category_category
                                     foreign key (category_code)
                                         references category(category_code)
);
create table product(
                        product_code int primary key,
                        product_name varchar(200),
                        color varchar(50),
                        cost int,
                        price int,
                        product_category_code varchar(10) not null,
                        constraint fk_product_product_category
                            foreign key (product_category_code)
                                references product_category(product_category_code)
);

create table customer(
                         customer_code int primary key,
                         region_code int not null,
                         customer_name varchar(100),
                         gender char(1),
                         birth_date date,
                         constraint fk_customer_region
                             foreign key (region_code)
                                 references region(region_code)
);

create table sales(
                      sales_date timestamp not null,
                      product_code int not null,
                      customer_code int not null,
                      promotion_code int not null,
                      channel_code int not null,
                      quantity int,
                      unit_price int,
                      constraint fk_sales_product
                          foreign key (product_code)
                              references product(product_code),
                      constraint fk_sales_customer
                          foreign key (customer_code)
                              references customer(customer_code),
                      constraint fk_sales_promotion
                          foreign key (promotion_code)
                              references promotion(promotion_code),
                      constraint fk_sales_channel
                          foreign key (channel_code)
                              references channel(channel_code)
);