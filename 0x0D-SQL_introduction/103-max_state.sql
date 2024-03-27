-- displays max temparature of each state (ordered by state name)
-- does not fail

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
