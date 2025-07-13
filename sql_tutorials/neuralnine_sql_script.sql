# Show all existing DBs
SHOW DATABASES;

# Check how DBs are strctured
SELECT * FROM information_schema.schemata;

# Open tutorialdb
USE tutorialdb;

# Show tables in open DB
SHOW TABLES;

# Create table fields
CREATE TABLE IF NOT EXISTS people (
  p_id integer PRIMARY KEY,
  p_name varchar(255),
  p_age integer,
  p_height float
);

# Show data from all columns
SELECT * FROM tutorialdb.people; # Currently empty

# Fill specified fields only
INSERT INTO tutorialdb.people (p_id, p_name) VALUES (1, 'Mike');

# Fill all fields
INSERT INTO tutorialdb.people VALUES (2, 'John', 78, 180);

# Insert many new records
INSERT INTO tutorialdb.people
  (p_id, p_name, p_age, p_height)
VALUES
  (3, 'Anna', 28, 180),
  (4, 'Bob', 38, 178),
  (5, 'Kate', 48, 182),
  (6, 'James', 55, 183),
  (7, 'Samuel', 38, 181),
  (8, 'Lisa', 28, 177);

SELECT * FROM tutorialdb.people;

# Select specific columns only
SELECT p_name, p_age FROM tutorialdb.people;

# Get specific fields, only for records that meet a conditional
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;

# Age 55 or younger
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age <= 55;

# Age is exactly 38
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age = 38;

# Age is NOT 28
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age <> 28;

# Age in in their 40s
SELECT p_name, p_age FROM tutorialdb.people
WHERE
  p_age >= 40
  AND p_age < 50;

# Where an age value in defined
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age IS NOT NULL;

# Get name & height for all people 18+ yo
SELECT p_name, p_height FROM tutorialdb.people
WHERE p_age >= 18;

# Get name & height for all people not <18yo
SELECT p_name, p_height FROM tutorialdb.people
WHERE NOT p_age < 18;

# ALWAYS USE PRIMARY KEY to alter/delete existing records
UPDATE tutorialdb.people
SET
  p_age = 30,
  p_height = 179
WHERE p_id = 1;

SELECT * FROM tutorialdb.people;

# Delete James (p_id = 6)
DELETE FROM tutorialdb.people
WHERE p_id = 6;

# Delete all records over 50yo
DELETE FROM tutorialdb.people
WHERE p_age > 50;

# Activate safe update mode
SET SQL_SAFE_UPDATES = 1;

# Add new record
INSERT INTO tutorialdb.people (p_id, p_name, p_height)
  VALUES (10, 'James', 178.56);
# Alter height column to be an integer (James' Ht -> 179)
ALTER TABLE tutorialdb.people
  MODIFY p_height int;

# Change name of p_height to p_ht; keep as integer
ALTER TABLE tutorialdb.people
  CHANGE COLUMN p_height p_ht
    int;
# Change back to p_height (do not need to specify definiton)
ALTER TABLE tutorialdb.people
  RENAME COLUMN p_ht TO p_height;

# Add new column
ALTER TABLE tutorialdb.people
  ADD COLUMN IF NOT EXISTS p_weight float;
# Drop the new column
ALTER TABLE tutorialdb.people
  DROP COLUMN IF EXISTS p_weight;

SELECT * FROM tutorialdb.people;

# Create a new people table w/ constraints
DROP TABLE IF EXISTS tutorialdb.people;
CREATE TABLE IF NOT EXISTS people (
  p_id int PRIMARY KEY,
  p_name varchar(255) NOT NULL,
  p_age int DEFAULT 21,
  p_ssn char(32) UNIQUE,
  CONSTRAINT age_constraint CHECK (
    p_age >= 0  # Must be non-negative
    AND p_age <= 125
  )
);
INSERT INTO tutorialdb.people (p_id, p_name) VALUES (1, 'Mike');
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn) VALUES (2, 'Jane', 25, '123456789');
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn) VALUES (3, 'Angela', 54, '987654321');
SELECT * FROM tutorialdb.people;

# Create a new people table w/ constraints, and that auto-increments p_id
DROP TABLE IF EXISTS tutorialdb.people;
CREATE TABLE IF NOT EXISTS people (
  p_id int PRIMARY KEY AUTO_INCREMENT,
  p_name varchar(255) NOT NULL,
  p_age int DEFAULT 21,
  p_ssn char(32) UNIQUE,
  CONSTRAINT age_constraint CHECK (
    p_age >= 0  # Must be non-negative
    AND p_age <= 125
  )
);
INSERT INTO tutorialdb.people (p_name) VALUES
  ('Mike'),
  ('John');
SELECT * FROM tutorialdb.people;

# Unique field combos
DROP TABLE IF EXISTS tutorialdb.people;
CREATE TABLE IF NOT EXISTS people (
  p_id int PRIMARY KEY AUTO_INCREMENT,
  p_firstname varchar(255),
  p_lastname varchar(255),
  CONSTRAINT name_constraint UNIQUE (
    p_firstname, p_lastname
  )
);
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('John', 'Doe'),
  ('John', 'Smith');
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('Jane', 'Doe'),
  ('Jane', 'Smith');
SELECT * FROM tutorialdb.people;

# Now truncate the data (to remove conflicts), and add unique last name as a constraint
TRUNCATE TABLE tutorialdb.people;
ALTER TABLE tutorialdb.people
  ADD CONSTRAINT unique_lastname UNIQUE (p_lastname);
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('John', 'Doe'),
  ('John', 'Smith');

# Create new table
DROP TABLE IF EXISTS tutorialdb.people;

CREATE TABLE IF NOT EXISTS people (
  p_id int PRIMARY KEY AUTO_INCREMENT,
  p_name varchar(255),
  p_age int,
  p_height float,
  p_sex enum('male', 'female')
);

INSERT INTO tutorialdb.people (p_name, p_age, p_height, p_sex) VALUES
  ('Mike', 55, 188, 'male'),
  ('Anna', 55, 182, 'female'),
  ('Lisa', 22, 167, 'female'),
  ('Bob', 34, 178, 'male'),
  ('John', 29, 180, 'male'),
  ('Jeff', 89, 182, 'male'),
  ('Angela', 77, 180, 'female'),
  ('Samuel', 55, 175, 'male'),
  ('Kate', 27, 167, 'female'),
  ('Andrew', 23, NULL, 'male'),
  ('Jim', 65, 187, 'male');

SELECT * FROM tutorialdb.people;

# Get everyone over 30
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;

# Get unique people over 30
SELECT DISTINCT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;

# Get a list of every first name in the table
SELECT DISTINCT p_name FROM tutorialdb.people;

# Get all people aged exactly 55 or 65yo
SELECT * FROM tutorialdb.people
WHERE p_age IN (55, 65);

# Get all people whose names start w/ M
SELECT * FROM tutorialdb.people
WHERE p_name LIKE 'M%';

# Get all people whose names end w/ a
SELECT * FROM tutorialdb.people
WHERE p_name LIKE '%A';

# Get all people w/ J anywhere in their name (incl. beginning/end)
SELECT * FROM tutorialdb.people
WHERE p_name LIKE '%J%';

# Display table with nicely named 'Name' & 'Age' columns
SELECT
  p_name AS 'Names Starting with A',
  p_age AS 'Age'
FROM tutorialdb.people
WHERE p_name LIKE 'A%';

# Sum age column
SELECT sum(p_age) AS 'Age Sum' FROM tutorialdb.people;

# Mean height for female
SELECT avg(p_height) AS 'Mean Female Height' FROM tutorialdb.people
  WHERE p_sex = 'female';
# Mean height for male
SELECT avg(p_height) AS 'Mean Female Height' FROM tutorialdb.people
  WHERE p_sex = 'male';

SELECT * FROM tutorialdb.people;

# Mean height, grouped by sex
SELECT
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;
# Same, with sexes displayed for readability
SELECT
  p_sex,
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;

# Mean age & height, grouped by sex
SELECT
  avg(p_age) AS 'Mean Age',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;

# Min/Max/Mean height, grouped by sex
SELECT
  min(p_height) AS 'Min Height',
  max(p_height) AS 'Max Height',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;

# Mean height, grouped by senior citizen status
SELECT
  p_age >= 65 AS 'Senior?',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_age >= 65;

# Mean height by male/female & senior status (1/0)
SELECT
  p_sex AS 'Sex',
  p_age >= 65 AS 'Senior?',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex, p_age >= 65;

# Order by age, ascending
SELECT * FROM tutorialdb.people
ORDER BY p_age;
# Order by age, descending
SELECT * FROM tutorialdb.people
ORDER BY p_age DESC;

# Order ascending age, then by descending height
SELECT * FROM tutorialdb.people
ORDER BY p_age, p_height DESC;

# Show only 1st 8 rows of a table
SELECT * FROM tutorialdb.people
LIMIT 8;

# Show records of the 8 tallest people
SELECT * FROM tutorialdb.people
ORDER BY p_height DESC
LIMIT 8;
