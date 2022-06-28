-- 联合查询(用得少)

SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill 
WHERE CardID='C00005'
-- 选择以 CardID 显示,则要用 GROUP BY
GROUP BY CardID
-- UNION 合并
UNION 
SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill
WHERE CardID='C00004'
GROUP BY CardID;


SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill 
WHERE CardID='C00005'OR CardID='C00004'
GROUP BY CardID
-- EXPECT 集合的差,上减下
EXCEPT
SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill
WHERE CardID='C00004'OR CardID='C00003'
GROUP BY CardID;


SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill 
WHERE CardID='C00005'OR CardID='C00004'
GROUP BY CardID
-- INTERSECT 求交集
INTERSECT
SELECT CardID AS 卡号,SUM(payamount) AS 消费总额
FROM Table_Salebill
WHERE CardID='C00004'OR CardID='C00003'
GROUP BY CardID;

-- 联接查询

-- 内联接 JOIN

SELECT StudentID AS 学号,SUM(payamount) AS 消费总额
FROM Table_Student A JOIN Table_Salebill B
ON A.CardID=B.CardID
WHERE saledate='2021-07-05'
GROUP BY StudentID
HAVING SUM(payamount)>20;

-- 左联接 LEFT JOIN
SELECT *
FROM Table_Student A LEFT JOIN Table_Salebill B
ON A.CardID=B.CardID

-- 右联接 LEFT JOIN
SELECT *
FROM Table_Salebill B RIGHT JOIN Table_Student A
ON A.CardID=B.CardID

-- 完全连接 FULL JOIN
SELECT *
FROM Table_Salebill B FULL JOIN Table_Student A
ON A.CardID=B.CardID


-- 嵌套查询
-- 子查询不能用 ORDER BY

-- IN 
SELECT StudentID,Sname,Sex,School
FROM Table_Student
WHERE School in
(SELECT School FROM Table_Student
WHERE Sname='刘杰');

-- 等于 =
SELECT CardID,payamount 
FROM Table_Salebill
WHERE payamount=
(SELECT MAX(payamount) FROM Table_Salebill);

-- EXISTS
-- 没有在2号机器上消费过的饭卡号
SELECT CardID
FROM Table_Student
WHERE NOT EXISTS
(SELECT * FROM Table_Salebill
WHERE MachineID='00000011' AND CardID=Table_Student.CardID)

-- 找出吃过所有食堂的学生
SELECT Sname
FROM Table_Student
WHERE NOT EXISTS
(SELECT * FROM Table_Salebill
WHERE NOT EXISTS  
(SELECT * FROM Table_Machine
WHERE Table_Salebill.CardID=Table_Student.CardID AND Table_Salebill.MachineID=MachineID));