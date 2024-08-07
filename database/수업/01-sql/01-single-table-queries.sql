-- 01. Querying data
SELECT 
    LastName 
FROM    
    employees;

SELECT 
    LastName, FirstName 
FROM    
    employees;

SELECT
    *
FROM
    employees;

SELECT
    FirstName AS '이름'
FROM
    employees;

SELECT
    NAME, 
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks;


-- 02. Sorting data
SELECT 
    FirstName
FROM
    employees
ORDER BY    
    FirstName;

SELECT 
    FirstName
FROM
    employees
ORDER BY    
    FirstName DESC;

SELECT
    Country, City
FROM
    customers
ORDER BY
    Country DESC,
    City ASC;

SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;

-- NULL 정렬 예시
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo DESC;


-- 03. Filtering data
SELECT DISTINCT
    Country
FROM
    customers
ORDER BY 
    Country;

SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague';

SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City != 'Prague';

SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL
    AND Country = 'USA';

SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL
    OR Country = 'USA';

SELECT
    Name, Bytes
FROM
    tracks
WHERE
    -- Bytes >= 10000
    -- AND Bytes <= 500000;
    Bytes BETWEEN 100000 AND 500000
ORDER BY
    Bytes;

SELECT
    LastName, FirstName, Country
From 
    customers
WHERE
    -- country = 'Canada'
    -- OR country = 'Germany'
    -- OR country = 'France';
    Country NOT IN ('Canada', 'Germany', 'France');

SELECT
    LastName, FirstName
FROM 
    customers
WHERE 
    LastName LIKE '%son';

SELECT
    LastName, FirstName
FROM
    customers
WHERE
    FirstName LIKE '___a';

SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
LIMIT
    7;

SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    Bytes DESC
-- LIMIT
--     3, 4;
    LIMIT 4 OFFSET 3;

-- 04. Grouping data
SELECT
    Country, COUNT(*)
FROM
    customers
GROUP BY
    Country;

SELECT
    Composer, AVG(Bytes) AS avg0fBytes
FROM
    tracks
GROUP BY
    Composer
ORDER BY
    avg0fBytes DESC;

SELECT
    Composer, 
    AVG(Milliseconds / 60000) AS avgOfMinute
From
    tracks
GROUP BY
    composer
HAVING
    avgOfMinute < 10;