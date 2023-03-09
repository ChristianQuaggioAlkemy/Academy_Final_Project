{{config(
    re_data_monitored=true,
    materialized="table",
    tag="datamart"
)}}


SELECT 
    e.data,
    e.country,
    e.latitude,
    e.longitude,
    e.mag,
    e.is_monday,
    e.is_tuesday,
    e.is_wednesday,
    e.is_thursday,
    e.is_friday,
    i.adjclose, 
    i.index_variation
FROM 
    {{ ref('earthquake_data_dummies') }} e
    LEFT JOIN {{ ref('index_variation') }} i
    ON e.data = i.data


