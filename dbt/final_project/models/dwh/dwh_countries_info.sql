{{config(
    re_data_monitored=true,
    materialized="table",
    tag="dwh"
)}}
with source as (
    select * from {{ source('public', 'countries_info') }}
)
select
    *
from source