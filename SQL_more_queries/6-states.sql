-- Script to create the 'states' table in the 'hbtn_0d_usa' database
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each state
    name VARCHAR(256) NOT NULL           -- Name of the state, cannot be null
);

