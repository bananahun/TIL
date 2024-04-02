--1
SELECT
    *
FROM
    users
WHERE
    age >= 30
AND
    balance >= 1000;
--2
SELECT
    *
FROM
    users
WHERE
    balance <= 1000
AND
    age <= 20;
--3
SELECT
    *
FROM
    users
WHERE
    first_name
like 
    '현%'
AND
    country = '제주특별자치도'
ORDER BY
    age DESC
LIMIT
    1;
--4
SELECT
    *
FROM
    users
WHERE
    last_name = '박'
AND
    age >= 25
ORDER BY
    age
limit 
    1;
--5
SELECT
    *
FROM
    users
WHERE
    first_name = '재은'
OR
    first_name = '영일'
ORDER BY
    balance DESC
LIMIT
    1;
--6
SELECT 
    *
FROM
    users
GROUP BY
    country
ORDER BY
    MAX(balance) DESC;
--7
SELECT
    *
FROM
    users
WHERE
    age >= 30
AND
    (SELECT
        AVG(balance)
    FROM    
        users
    WHERE
        age >= 30) <= balance;