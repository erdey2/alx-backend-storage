-- create a table with constraint

IF NOT EXISTS CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTO_INCREMENT,
       email STRING(255) NOT NULL UNIQUE,
       name STRING(255)
);
