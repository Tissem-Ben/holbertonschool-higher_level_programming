Python Object-Relational Mapping (ORM) Project
This project demonstrates how to connect a Python script to a MySQL database and use SQLAlchemy to simplify database interactions through Object-Relational Mapping (ORM). The project consists of scripts to connect to a MySQL database, retrieve data, and perform operations without needing raw SQL commands.Python ORM Project
This project demonstrates how to connect Python to a MySQL database using both raw SQL queries with MySQLdb and Object-Relational Mapping (ORM) with SQLAlchemy.

Overview
Connect to a MySQL database from Python.
Retrieve and display data from the states table.
Use SQLAlchemy ORM to simplify database interactions.
Requirements
Python: 3.8.5
MySQL: 8.0.x
MySQLdb: 2.0.x
SQLAlchemy: 1.4.x
OS: Ubuntu 20.04 LTS

1 Setup
sudo apt update
sudo apt install mysql-server python3-dev libmysqlclient-dev
sudo pip3 install mysqlclient

2 Install SQLAlchemy:
sudo pip3 install SQLAlchemy

3 Create Database: Run 0-select_states.sql to set up the database and table.

