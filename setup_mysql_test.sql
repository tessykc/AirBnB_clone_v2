-- hbnb_test_db set up
-- new user hbnb_test (in localhost)
-- password hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on the database hbnb_test_db
-- hbnb_test should have SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER  IF NOT 'hbnb_test'@'localhost' IDENTIFIRD BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
