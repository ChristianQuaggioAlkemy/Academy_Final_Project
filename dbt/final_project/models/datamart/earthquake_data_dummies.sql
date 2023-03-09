
{{config(
    re_data_monitored=true,
    materialized="table",
    tag="datamart"
)}}

SELECT *,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 1 THEN 1 ELSE 0 END AS is_monday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 2 THEN 1 ELSE 0 END AS is_tuesday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 3 THEN 1 ELSE 0 END AS is_wednesday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 4 THEN 1 ELSE 0 END AS is_thursday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 5 THEN 1 ELSE 0 END AS is_friday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 6 THEN 1 ELSE 0 END AS is_saturday,
  CASE WHEN EXTRACT(DOW FROM d.Data) = 0 THEN 1 ELSE 0 END AS is_sunday,
  CASE WHEN LAG(mag) OVER (ORDER BY d.data) IS NULL THEN 0 ELSE 1 END AS eq_check_yesterday
FROM {{ ref('dwh_earthquake_data') }} d
