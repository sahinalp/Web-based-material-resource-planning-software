CREATE TABLE SalesOrders (
    Id SERIAL PRIMARY KEY,
    Code VARCHAR(20) NOT NULL,
    Total INT NOT NULL,
    Shipped INT NOT NULL,
    OrderNo VARCHAR(10)
)

CREATE TABLE Stock (
    Id SERIAL PRIMARY KEY,
    Code VARCHAR(50) NOT NULL,
    Quantity REAL NOT NULL,
    Unit VARCHAR(10)
)

INSERT INTO SalesOrders (Id, Code, Total , Shipped, OrderNo)
VALUES (1, 'model_s' , 200, 30 , 'PO-001');

INSERT INTO SalesOrders (Id, Code, Total , Shipped, OrderNo)
VALUES (2, 'model_s' , 100, 0 , 'PO-002');

INSERT INTO SalesOrders (Id, Code, Total , Shipped, OrderNo)
VALUES (3, 'semi' , 10, 1 , 'PO-003');

INSERT INTO SalesOrders (Id, Code, Total , Shipped, OrderNo)
VALUES (4, 'semi' , 4, 0 , 'PO-003');



INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (1, 'wheel' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (2, 'steering_wheel' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (3, 'seat' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (4, 'right_mirror' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (5, 'left_mirror' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (6, 'mid_mirror' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (7, 'big_right_mirror' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (8, 'big_left_mirror' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (9, 'lcd_monitor' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (10, 'glass' , 0 , 'cm2');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (11, 'right_mirror_holder' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (12, 'left_mirror_holder' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (13, 'mid_mirror_holder' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (14, 'big_right_mirror_holder' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (15, 'big_left_mirror_holder' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (16, 'camera' , 0 , 'pieces');

INSERT INTO Stock (Id, Code, Quantity , Unit)
VALUES (17, 'polymer' , 0 , 'kg');

