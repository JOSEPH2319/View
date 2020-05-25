import sqlite3

conn = sqlite3.connect('chinook.sqlite')
library = conn.cursor()


# Question #1
CREATE VIEW
EXAMPLE AS
SELECT *
FROM library
WHERE name LIKE 'Grunge';


# Question #2
SELECT MAX(money)
FROM library
GROUP BY TV_SHOW;


# Question #3
SELECT countries
FROM library
ORDER BY Jane Peacock;


# Question #4
SELECT customers
FROM library
WHERE company > 0;


# Question #5
SELECT AVG(money)
FROM library
GROUP BY customer
HAVING gmail_adress

