import sqlite3

conn = sqlite3.connect('chinook.sqlite')
library = conn.cursor()


SELECT *
FROM library
WHERE name LIKE 'Grunge';


SELECT MAX(money)
FROM library
GROUP BY TV_SHOW;


SELECT countries
FROM library
ORDER BY Jane Peacock;

SELECT customers
FROM library
WHERE company > 0;

SELECT AVG(money)
FROM library
GROUP BY customer
HAVING gmail_adress
