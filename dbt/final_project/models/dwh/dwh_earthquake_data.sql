{{config(
    re_data_monitored=true,
    materialized="table",
    tag="dwh"
)}}
with source as (
    select * from {{ source('public', 'earthquake_data') }}
)
select
    *
from source