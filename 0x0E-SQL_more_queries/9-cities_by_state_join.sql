-- Select all cities with corresponding state names
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities
JOIN (states) ON cities.state_id = states.id
ORDER BY id ASC;
