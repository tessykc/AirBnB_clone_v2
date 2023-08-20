-- create database hbnb_dev_db
-- new user hbnb_dev in localhost
-- password set to hbnb_dev_pwd
-- priviledges given to hbnb_dev on hbnb_dev_db
-- hbnb_dev have select priviledge on db performance_schema
-- script won't fail if hbnb_dev or hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
