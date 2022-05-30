-- DELETE FROM restaurants WHERE place_id = 'ChIJgR_qY1cIAWAR_G-414hVF-A'
SELECT place_id, name, genre
FROM restaurants
WHERE genre in (0,1,2,3,4)