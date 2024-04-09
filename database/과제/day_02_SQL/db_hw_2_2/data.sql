CREATE TABLE orders(
    order_id INT,
    order_date DATE,
    total_amount RARE
);

INSERT INTO orders (order_id, order_date, total_amount) 
VALUES
    (1, '2023-07-15', 50.99),
    (2, '2023-07-16', 75.5),
    (3, '2023-07-17', 30.25);

CREATE TABLE customers (
    customer_id INT,
    name TEXT,
    email TEXT,
    phone TEXT
);

INSERT INTO customers (customer_id, name, email, phone) 
VALUES
    (1, '허균', 'john.doe@example.com', '010-1234-1234' ),
    (2, '김영희', 'jane.smith@example.com', '010-5678-5678'),
    (3, '이철수', 'michael.johnson@example.com', '010-1234-5678' );

SELECT
    *
FROM
    orders;

SELECT
    *
FROM
    customers;


DELETE FROM 
    orders 
WHERE   
    order_id = 3;


UPDATE 
    customers 
SET 
    name = '홍길동' 
WHERE 
    customer_id = 1;
