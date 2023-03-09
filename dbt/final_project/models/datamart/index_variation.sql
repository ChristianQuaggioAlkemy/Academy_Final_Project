{{config(
    re_data_monitored=true,
    materialized="table",
    tag="datamart"
)}}


SELECT 
    d.data,
    COALESCE(d.adjclose, (
        SELECT adjclose 
        FROM {{ ref('dwh_index_stock_data') }} 
        WHERE adjclose IS NOT NULL AND data < d.data 
        ORDER BY data DESC 
        LIMIT 1
    )) AS adjclose,
    COALESCE((d.adjclose / LAG(d.adjclose) OVER (ORDER BY d.data) - 1) * 100, 0) AS index_variation
FROM 
    {{ ref('dwh_index_stock_data') }} d


