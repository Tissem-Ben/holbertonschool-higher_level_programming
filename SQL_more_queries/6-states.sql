-- Script to create the 'states' table in the 'hbtn_0d_usa' database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;  -- Create the database if it doesn't exist
USE hbtn_0d_usa;                             -- Use the created database

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each state
    name VARCHAR(256) NOT NULL               -- Name of the state, cannot be null
); 

-- Insert initial data into states table
INSERT INTO states (name) VALUES 
('California'), 
('Arizona'), 
('Texas');

