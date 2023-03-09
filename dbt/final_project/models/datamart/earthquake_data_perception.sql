
{{config(
    re_data_monitored=true,
    materialized="table",
    tag="datamart"
)}}

SELECT *,
    CASE 
        WHEN mag < 6.0 THEN 'medium'
        WHEN mag >= 6.0 AND mag < 7 THEN 'intense'
        WHEN mag >= 7 AND mag < 8 THEN 'extremely intense' 
        WHEN mag >= 8 AND mag < 9 THEN 'catastrophic'
        WHEN mag >= 9 THEN 'apocalyptic'
        ELSE NULL
    END AS perception
FROM {{ ref('dwh_earthquake_data') }}
WHERE mag IS NOT NULL