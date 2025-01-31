-- Use the provided database (this is an argument passed to the mysql command)
USE alx_book_store;

-- Query the INFORMATION_SCHEMA to get the full description of the 'Books' table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
