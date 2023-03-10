
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
	ed.perception,
	ci.population,
	ci.urbandensity
FROM {{ ref('earthquake_data_perception') }} ed
JOIN {{ ref('dwh_countries_info') }} ci
	ON ci.code = ed.country
