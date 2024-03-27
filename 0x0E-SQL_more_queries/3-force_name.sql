-- creates the table force_name on server
-- database name will be passed as an argument in the command
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
