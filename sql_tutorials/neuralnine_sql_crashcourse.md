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

### See & Manipulate Table Data

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

#### Conditional Selections


