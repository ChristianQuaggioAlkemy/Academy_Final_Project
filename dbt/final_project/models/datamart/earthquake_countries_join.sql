
{{config(
    re_data_monitored=true,
    materialized="table",
    tag="datamart"
)}}

SELECT
	ed.data,
	ed.latitude,
	ed.longitude,
	ed.depth,
	ed.mag,
	ci.code,
	ci.country,
	ci.population,
	ci.urbandensity
FROM {{ ref('dwh_countries_info') }} ci
LEFT JOIN {{ ref('earthquake_data_perception') }} ed
	ON ci.code = ed.country
