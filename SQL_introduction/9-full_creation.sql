-- Create table second_table in the database hbtn_0c_0 and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into second_table, avoiding duplicate entries
INSERT IGNORE INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
