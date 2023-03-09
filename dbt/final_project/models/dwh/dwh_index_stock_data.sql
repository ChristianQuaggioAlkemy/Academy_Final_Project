{{config(
    re_data_monitored=true,
    materialized="table",
    tag="dwh"
)}}
with source as (
    select * from {{ source('public', 'index_stock_data') }}
)
select
    *
from source