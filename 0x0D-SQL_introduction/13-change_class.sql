-- remove all records with a score <= 5 in second_table
-- does not fail

DELETE FROM second_table
WHERE score <= 5;
