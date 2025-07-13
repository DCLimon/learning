SQL Crash Course
================

Tutorial from NeuralNine YouTube SQL Crash Course video.<br>
[Link to video.](https://youtu.be/7cIG41gjHB4?si=QJow7ptEtJ7ClKtU)

Setup
-----

* RDBMS framework: MariaDB
* DB Admin Tool: DBeaver


Getting Up & Running
--------------------

1. MariaDB was downloaded
2. Local MariaDB server was made
3. DBeaver Community Edition was downloaded
4. DBeaver-CE was provided with the connection to local server 


### Show All Databases

In the localhost console:
```mariadb
SHOW DATABASES;
```


### Create New DB

This will work, but will error out if DB of same name already exists:
```mariadb
CREATE DATABASE tutorialdb;
```

Preferred method:<br>
(Will throw a warning instead of an error if DB already exists)
```mariadb
CREATE DATABASE IF NOT EXISTS tutorialdb;
```

`tutorialdb` will now show up if `SHOW DATABASES;` command is repeated.

If we wanted to do this with default presets like character sets and a comment,
we could do this at creation via:
```mariadb
CREATE DATABASE IF NOT EXISTS tutorialdb
    CHARACTER SET='utf8mb4'
    COLLATE='utf8mb4_general_ci'
    COMMENT='NeuralNine YT Tutorial';
```


### Change Global DB Info

You can check the "information schemata" for all DBs to see their names, default
character sets, etc.
```mariadb
SELECT * FROM information_schema.schemata;
```

If we wanted to alter the default character set for `tutorialdb`, and, as a corollary,
how it collates the characters, we could run:
```mariadb
ALTER DATABASE tutorialdb CHARACTER SET='utf8mb4' COLLATE='utf8mb4_general_ci';
```

Add a comment about the DB with:
```mariadb
ALTER DATABASE tutorialdb COMMENT='NeuralNine YT Tutorial';
```


### Delete DB from Existence

Be careful!
```mariadb
DROP DATABASE tutorialdb;
```


### Open (Use) a DB

Need to tell server which DB we want to "use" (open)
```mariadb
USE tutorialdb;
```


Working in a DB
---------------

You can check all available tables in the open DB via:
```mariadb
SHOW TABLES;
```


### Create a table

Let's create a `people` table, with columns:
* `p_id` (good practice to use `p_` to indicate that `id` identifies `people`)
  * data type: integer
  * constraints:
    * **Primary Key** for this table
* `p_name`
  * type: varchar up to 255 characters
* `p_age`
  * type: integer
* `p_height`
  * type: float

Let's do all this, and then show tables to make sure it was created properly
```mariadb
CREATE TABLE IF NOT EXISTS people (
    p_id integer PRIMARY KEY,
    p_name varchar(255),
    p_age integer,
    p_height float
);

SHOW TABLES;
```


#### Available Data Types

Common field data types include:
* Text types:
  * fixed-size text characters (e.g. 32 chars) = `CHAR(32)`
    * Note: fixed-size characters are usually faster than `VARCHAR`
  * variable-length text characters (e.g. *up to* 32 chars) = `VARCHAR(32)`
  * long text strings = `TEXT`
  * a enumerated multiple-choice list of strings, from which you can choose one = `ENUM()`
    * e.g. favorite programming language: `ENUM('Python', 'C++', 'R')`
      * You are not allowed to pick `'Rust'` as a favorite, b/c it has not been enumerated
* Numeric types:
  * integer: `INT` or `INTEGER`
  * `FLOAT`
  * float to a specified number of decimal places = `DECIMAL`
  * `BOOLEAN`
* Date/Time types:
  * `DATE`
  * `TIME`
  * `DATETIME`
  * `TIMESTAMP`
* Compound Structures:
  * `DOUBLE` (presumably tuple w/ 2 members?)


### Add Data to Tables

With `people` table created, let's see all columns in the (currently empty) table
```mariadb
SELECT * FROM people;
```

Can also specify which DB people is in via
```mariadb
SELECT * FROM tutorialdb.people;
```

And can set a temporary alias `p` for the `people` table via
```mariadb
SELECT * FROM tutorialdb.people p;
```

***

Now let's insert some data into the table. We can do this 2 ways:
* List values for all fields in that record
* Specify which fields will be filled, and values for each of those fields
  * Also allows you to enter values for fields out of order (compared to the column order)
```mariadb
# Values for only specified fields
INSERT INTO tutorialdb.people (p_id, p_name) VALUES (1, 'Mike');

# Values for all fields
INSERT INTO tutorialdb.people VALUES (2, 'John', 78, 180);
```

When inserting data (either method), **a value for the primary key must always be
passed** (unless a default value is set, which would probably be stupid for a primary
key or an ID number)

***

Now insert many records in a single query execution
```mariadb
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
```


### Get Data from Tables

View only specified columns in a table (but all rows)
```mariadb
# Select specific columns only
SELECT p_name, p_age FROM tutorialdb.people;
```

Now retrieve those same specified fields, but only for records that meet a conditional
```mariadb
# Get specific fields, only for records that meet a conditional (age > 30)
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;

# 55yo or younger
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
```

Can also filter based on table fields that are not being displayed.<br>
e.g. Get height of all legal adults:
```mariadb
# Both queries have identical output:

# Get name & height for all people 18+ yo
SELECT p_name, p_height FROM tutorialdb.people
WHERE p_age >= 18;

# Get name & height for all people not <18yo
SELECT p_name, p_height FROM tutorialdb.people
WHERE NOT p_age < 18;
```


Update, Delete, & Alter Existing Data
-------------------------------------

### Altering Records

You can alter fields for existing records via the `UPDATE` command.

**Must always use conditions BASED ON PRIMARY KEY to specify WHICH recordS are being
updated!** Only the primary key is guaranteed to be unique in that table.

Example: We want to set Mike's age to 30yo & Ht to 179cm<br>
* *Setting w/o a conditional would change the entire table's age/Ht:*
* *Setting with a non-unique conditional (e.g. first name) could affect unintended rows*
```mariadb
# NO -- sets entire table's age to 30yo
UPDATE tutorialdb.people SET p_age = 30;

# NO -- sets anyone named Mike's age to 30yo &
UPDATE tutorialdb.people SET p_age = 30
WHERE p_name = 'Mike';

# YES
UPDATE tutorialdb.people
SET
  p_age = 30,
  p_height = 179
WHERE p_id = 1;
```

### Deleting Records

Again, **NEVER DELETE RECORDS WITHOUT A `WHERE` CONDITIONAL**. Also use extreme
caution (i.e. test using `SELECT` first) when using a non-unique conditional.
```mariadb
# Delete James (p_id = 6)
DELETE FROM tutorialdb.people
WHERE p_id = 6;

# Delete all records over 50yo
DELETE FROM tutorialdb.people
WHERE p_age > 50;
```

#### Safe Update Mode

In MySQL & MariaDB, you can activate "safe update mode" via:
```mariadb
# Deactivate
SET SQL_SAFE_UPDATES = 0;

# Activate
SET SQL_SAFE_UPDATES = 1;
```

Safe update mode blocks all `UPDATE` & `DELETE` queries that are executed without
either:
* A `WHERE` clause + an Index (aka Key) Column
* A `LIMIT` clause

### Altering Fields

First add a new record
```mariadb
INSERT INTO tutorialdb.people (p_id, p_name, p_height)
  VALUES (10, 'James', 178.56);
```

Now change the p_height column to be an `INTEGER` type. James' Ht will go from
178.56cm to 179cm
```mariadb
# Alter height column to be an integer (James' Ht -> 179)
ALTER TABLE tutorialdb.people
  MODIFY p_height int;
```

Change name of `p_height` to `p_ht`
```mariadb
# Option 1
ALTER TABLE tutorialdb.people
  CHANGE COLUMN p_height p_ht
    int; # Must specify data type (incl. NULL/NOT NULL) when changing name
    
# Option 2: Do not need to specify definition
ALTER TABLE tutorialdb.people
  RENAME COLUMN p_ht TO p_height;
```

Add a weight column, then drop it
```mariadb
# Add new column
ALTER TABLE tutorialdb.people
  ADD COLUMN IF NOT EXISTS p_weight float;

# Drop the new column
ALTER TABLE tutorialdb.people
  DROP COLUMN IF EXISTS p_weight;
```

### Removing Table Data

Clear all data from a table, but leave the (empty) table in the DB:
```mariadb
TRUNCATE TABLE people;
```

Delete the table from the DB:
```mariadb
DROP TABLE IF EXISTS people;
```

Constraints
-----------

### Primary keys

Primary keys uniquely identify records such that when referenced, they point to one
and only one row.

Primary keys can be:
* A single field, e.g. an MRN
* A combination of rows, e.g. Name + DOB
  * 2 records can have the same name, or the same DOB, but not both

Primary keys must:
* be unique to 1 and only 1 row
* can never be `NULL`

While MariaDB allows tables w/o primary keys, that is bad practice.

Set a primary key:
```mariadb
# Option 1A: p_id is PK
CREATE TABLE IF NOT EXISTS people (
    p_id integer PRIMARY KEY,
    p_name varchar(255),
    p_age integer,
    p_height float
);

# Option 1B: p_id is PK
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float,
    PRIMARY KEY (p_id)
);

# Option 2: Make p_id PK after table creation
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float
);
ALTER TABLE people
    ADD PRIMARY KEY (p_id)
    
# Option 3A: Make PK column called p_pk from p_id
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float,
    CONSTRAINT p_pk PRIMARY KEY (p_id)
);

# Option 3B: Make PK column after creation called p_pk from p_id
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float
);
ALTER TABLE people
    ADD CONSTRAINT p_pk
        PRIMARY KEY (p_id);

# Option 4A: Make combo of name+age the a PK column called p_pk
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255) NOT NULL ,
    p_age integer NOT NULL,
    p_height float,
    CONSTRAINT p_pk PRIMARY KEY (p_name, p_age)
);

# Option 4B: Make combo of name+age the PK column called p_pk after creation
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255) NOT NULL ,
    p_age integer NOT NULL,
    p_height float
);
ALTER TABLE people
    ADD CONSTRAINT p_pk
        PRIMARY KEY (p_name, p_age);
```


### Unique Keys

You can also specify unique keys, where they are not the primary key of the table,
but duplicate unique keys in multiple records are not allowed. Unique keys are
allowed to be `NULL`.

Create a primary & unique key
```mariadb
# Option 1: p_id is PK, p_name must be unique but is non-primary
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float,
    PRIMARY KEY (p_id),
    UNIQUE KEY (p_name)
);

# Option 2A: Make p_name a unique index called p_idx after creation
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float,
    PRIMARY KEY (p_id),
);
ALTER TABLE people
    ADD UNIQUE p_idx (p_name);

# Option 2B: Make p_name a unique index called p_idx after creation
CREATE TABLE IF NOT EXISTS people (
    p_id integer NOT NULL,
    p_name varchar(255),
    p_age integer,
    p_height float,
    PRIMARY KEY (p_id),
);
CREATE UNIQUE INDEX p_idx ON people(p_name);
```


### Other Constraints

Now let's make a new people table that satisfies the following constraints:
* `p_id` = integer
  * unique
  * not null
  * primary key
* `p_name` = up to 255-length character string
  * cannot be null
* `p_age` = integer
  * default to 21 if no age given
  * must be >= 0
  * must be <= 125
* `p_ssn` = 32-character string
  * CAN be null
  * MUST be unique, if it exists

```mariadb
# Create a new people table w/ constraints
DROP TABLE IF EXISTS tutorialdb.people;
CREATE TABLE IF NOT EXISTS people (
  p_id int PRIMARY KEY,
  p_name varchar(255) NOT NULL,
  p_age int DEFAULT 21,
  p_ssn char(32) UNIQUE,
  CONSTRAINT age_constraint CHECK (
    p_age >= 0,  # Must be non-negative
    p_age <= 125
  )
);
```

Now add some data
```mariadb
# RUNS: age defaults to 21, SSN is NULL
INSERT INTO tutorialdb.people (p_id, p_name) VALUES (1, 'Mike');

# FAILS: p_id (PK) must be unique
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (1, 'Jane', 25, '123456789');
# RUNS
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (2, 'Jane', 25, '123456789');


# FAILS: SSN cannot be duplicated
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (3, 'Angela', 54, '123456789');
# RUNS
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (3, 'Angela', 54, '987654321');


# FAILS: age cannot be negative
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (4, 'John', -10, '012345678');
# FAILS: age cannot be >125
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (4, 'John', 132, '012345678');
# RUNS
INSERT INTO tutorialdb.people (p_id, p_name, p_age, p_ssn)
    VALUES (4, 'John', -10, '012345678');
```


### Auto-Incrementing ID Column

If `p_id` is arbitrary and defined by the table itself, you can set it to automatically
increment when a new record is added.

Let's recreate this table with an auto-incrementing `p_id`
```mariadb
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
  ('Mike'), # p_id=1, age=21, SSN=NULL
  ('John'); # p_id=2, age=21, SSN=NULL

SELECT * FROM tutorialdb.people;
```


### Unique Column Combinations

Create a table w/ first name & last name. Neither the first name nor last name alone
need to be unique, but the full name must be unique.
```mariadb
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
```

Add data
```mariadb
# RUNS: Johns have different last names
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('John', 'Doe'),
  ('John', 'Smith')
);


# RUNS: Janes have different last names from each other, & different first names
# than the Johns
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('Jane', 'Doe'),
  ('Jane', 'Smith')
);

# FAILS: Jane Doe already exists
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES ('Jane', 'Doe');
```

### Adding Constraints to Existing Table

Let's truncate (remove all data from) the table, since it would cause a conflict.
Then, let's add the constraint that all last names must be unique.
```mariadb
# Now truncate the data (to remove conflicts), and add unique last name as a constraint
TRUNCATE TABLE tutorialdb.people;
ALTER TABLE tutorialdb.people
  ADD CONSTRAINT unique_lastname UNIQUE (p_lastname);
```

Add data
```mariadb
# RUNS: last names & full names are unique
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES
  ('John', 'Doe'),
  ('John', 'Smith');


# FAILS: full names are unique, but last name is a duplicate
INSERT INTO tutorialdb.people (p_firstname, p_lastname) VALUES ('Jane', 'Doe');
```


Advanced SQL Queries
--------------------

Create a new people table and insert some data
```mariadb
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
```


### Conditional Selections

Get names/ages for everyone over 30yo
```mariadb
# Get everyone over 30
SELECT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;
```

Get list of every first name that appears in the table. This is equivalent to
`df['name'].unique()`
```mariadb
# Get a list of every first name in the table
SELECT DISTINCT p_name FROM tutorialdb.people;
```

Only get unique **combos of names/ages** for people over 30yo. This is equivalent
to `df[['name', 'age']].unique()`
```mariadb
# Get unique people over 30
SELECT DISTINCT p_name, p_age FROM tutorialdb.people
WHERE p_age > 30;
```


### Pattern Matching

Get all members of a list.
`df.loc[df['age'].isin([55, 65])]`
```mariadb
SELECT * FROM people
WHERE p_age IN (55, 65);
```

`%` operator works as a wildcard
```mariadb
# Get all people whose names start w/ M
SELECT * FROM tutorialdb.people
WHERE p_name LIKE 'M%';

# Get all people whose names end w/ a
SELECT * FROM tutorialdb.people
WHERE p_name LIKE '%a';  # Case-insensitive; '%A' gives same results

# Get all people w/ J anywhere in their name (incl. beginning/end)
SELECT * FROM tutorialdb.people
WHERE p_name LIKE '%J%';
```

Can use aliases via `AS` to temporarily display different column names
```mariadb
# Display table with nicely named 'Name' & 'Age' columns
SELECT
  p_name AS 'Names Starting with A',
  p_age AS 'Age'
FROM tutorialdb.people
WHERE p_name LIKE 'A%';
```


### Aggregation Functions

Can use aggregation function operators sum/count/etc. columns values
```mariadb
# Sum up age column
SELECT sum(p_age) AS 'Age Sum' FROM tutorialdb.people;
```

Available aggregation fxns:
* `count()`
* `sum()`
* `avg()`
* `min()`
* `max()`

Get mean height of all females in the table<br>
Equivalent to `df.loc[df['sex'] == 'female']['height'].mean()`
```mariadb
# Mean height for females
SELECT avg(p_height) AS 'Mean Female Height' FROM tutorialdb.people
  WHERE p_sex = 'female';

# Mean height for males
SELECT avg(p_height) AS 'Mean Female Height' FROM tutorialdb.people
  WHERE p_sex = 'male';
```


### Group By

Similar to Pandas `groupby` method, this requires:
* table (DF) name
* 1 or more grouper columns
  * should generally use *categorical* or Boolean groupers
* 1 or more output columns, *each with an aggregation function*
  * should generally use numeric (integer/float/Boolean) output columns

Of note:
* in Pandas `groupby`, unless parameter `as_index=False`, the resulting DF's index *is* the values/categories of the grouper columns
  * this makes it easy to tell which row in the results corresponds to which grouper categories
* in SQL `GROUP BY`, the output rows simply have a numerical index, in order of observation of the grouper categories
  * You can fix this by making the grouper also an output column (see below)

* **Columns in the `SELECT` term, but NOT the `GROUP BY` term, must be wrapped in
an aggregation function** (o/w will error). <br>
* A column used as a grouper CAN appear naked in the `SELECT` term
  * in fact, as stated above (& shown below), this is a good idea to always do, so that the groups are properly labeled

To make the output clear, each SQL group-by will be given its equivalent Pandas `groupby`.

***

Mean height for each sex

`df.groupby(['sex'], observed=True)['height'].mean()` <br>
or <br>
`df.groupby(['sex'], observed=True)['height'].agg(['mean'])`

```mariadb
# Mean height, grouped by sex
SELECT
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;
```

Whereas Pandas would output:

|          |               |
|:---------|--------------:|
|          |      `height` |
| `sex`    |               |
| `male`   |  `188.666667` |
| `female` |  `174.000000` |

SQL will output:

|          |  Mean Height  |
|:---------|:-------------:|
| 1        |  181.666667   |
| 2        |      174      |

However, by including your grouper in your `SELECT` term, you can clarify this:
```mariadb
# Mean height grouped by sex, with sex displayed
SELECT
  p_sex AS 'Sex',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;
```
to look like this:

SQL output:

|          | p_sex  |  Mean Height  |
|:---------|:-------|:-------------:|
| 1        | male   |  181.666667   |
| 2        | female |      174      |

***

Mean age & height for each sex

`df.groupby(['sex'], observed=True)[['age', height']].mean()` <br>
or <br>
`df.groupby(['sex'], observed=True)[['age', 'height']].agg(['mean'])`

```mariadb
# Mean age & height, grouped by sex
SELECT
  p_sex AS 'Sex',
  avg(p_age) AS 'Mean Age',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;
```

***

Min, Max, & Mean height for each sex

`df.groupby(['sex'], observed=True)['height'].agg(['min', 'max', 'mean'])`

```mariadb
# Min/Max/Mean height, grouped by sex
SELECT
  p_sex AS 'Sex',
  min(p_height) AS 'Min Height',
  max(p_height) AS 'Max Height',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex;
```

***

You can also group by a conditional, instead of a normal categorical. The truth
value of the conditional is output as `0/1`.

`df.groupby([df['age'] >= 65], observed=True)['height'].agg(['mean'])`

```mariadb
# Mean height, grouped by senior citizen status
SELECT
  p_age >= 65 AS 'Senior?',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_age >= 65;
```

Or even just group by numeric values, though treating continuous numeric data as
a categorical gives dumb, useless output.

`df.groupby(df['age'], observed=True)['height'].agg(['mean'])`

```mariadb
# Mean height by age
SELECT
  p_age,
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_age;
```

***

You can also include multiple groups in the `GROUP BY` term, but *if you do so, make
sure each grouper is listed in the select term so that output is comprehensible.*

E.g. Get average height, grouped by male/female AND by senior citizen (65+) status 
(0/1) <br>
`df.groupby(['sex', df['age'] >= 65], observed=True)['height'].agg(['mean'])`

```mariadb
# Mean height by male/female & senior status (1/0)
SELECT
  p_sex AS 'Sex',
  p_age >= 65 AS 'Senior?',
  avg(p_height) AS 'Mean Height'
FROM tutorialdb.people
GROUP BY p_sex, p_age >= 65;
```

### Ordering results

Can use `ORDER BY` command to order the results (ascending is default)

Age, youngest to oldest:
```mariadb
# Order by age, ascending
SELECT * FROM tutorialdb.people
ORDER BY p_age;

# Same results:
SELECT * FROM tutorialdb.people
ORDER BY p_age ASC;
```

Age, oldest to youngest:
```mariadb
# Order by age, descending
SELECT * FROM tutorialdb.people
ORDER BY p_age DESC;
```

***

Can also use multi-layered `ORDER BY`. `ASC`/`DESC`/default applies to each respective `ORDER BY` group.

Order from youngest to oldest, and within an age, order tallest to shortest:
```mariadb
# Order ascending age, then by descending height
SELECT * FROM tutorialdb.people
ORDER BY p_age, p_height DESC;
```

### Limiting Output

The `LIMIT` clause only gives the first X number of results from the resulting
table.

* On its own, it can quickly show you how a table looks without having to retrieve the entire
table (very helpful if table is very large)
  * Show the 1st 8 rows of a table: `df.head(8)`

```mariadb
# Show only 1st 8 rows of a table
SELECT * FROM tutorialdb.people
LIMIT 8;
```

* Or it can be combined with `ORDER BY` to show the records w/ the X smallest/largest
values in a table
  * Show the 8 tallest people in the table: `df.sort_values(['height'], ascending=False).head(8)`

```mariadb
# Show records of the 8 tallest people
SELECT * FROM tutorialdb.people
ORDER BY p_height DESC
LIMIT 8;
```
