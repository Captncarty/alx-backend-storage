-- Lists all bands with Glam rock as their style,
-- ranked by their longevity
-- Column names must be: band_name & lifespan

-- Create a temporary table to store the bands and their lifespan
CREATE TEMPORARY TABLE temp_bands (
  band_name VARCHAR(100),
  lifespan INT
);

-- Insert the bands and their lifespan into the temporary table
INSERT INTO temp_bands (band_name, lifespan)
SELECT band_name,
       YEAR("2022-01-01") - YEAR(FROM_UNIXTIME(UNIX_TIMESTAMP(split, 'dd.mm.yyyy'))) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock';

-- List the bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, lifespan
FROM temp_bands
ORDER BY lifespan DESC;
