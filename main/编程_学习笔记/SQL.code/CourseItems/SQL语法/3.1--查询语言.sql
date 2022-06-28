-- SELECT语句

-- SELECT  
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY
-- 执行顺序  from->order by,最后select


SELECT * FROM Table_Card
-- SELECT 属性名 ( (AS)新命名) FROM 表
SELECT CardID AS 卡号 FROM Table_Card
-- 多项查询与命名
SELECT CardID AS 卡号,Balance AS 余额 FROM Table_Card
-- DISTINCT: 不显示重复项
SELECT DISTINCT School 学院 FROM Table_Student
-- TOP n 函数: 返回前 n 行
SELECT TOP 9 CardID AS 卡号,Balance AS 余额 FROM Table_Card

-- WHERE子句
SELECT StudentID 学号,School 学院, Sname 姓名
FROM Table_Student
WHERE School='计算机学院'

-- 其他操作符
SELECT CardID 饭卡号,MachineID 机器号,saledate 日期
FROM Table_Salebill
WHERE MachineID='00000011' AND saledate BETWEEN '2021-06-30' AND '2021-07-03'

-- LIKE模糊查询
SELECT StudentID 学号,School 学院, Sname 姓名,CardID 卡号
FROM Table_Student
WHERE CardID LIKE 'C____1' OR School LIKE '%机%'

-- ORDER BY排序
-- DESC 降序 / ASC 升序
SELECT CardID 饭卡号,Balance 余额
FROM Table_Card
ORDER BY Balance DESC,CardID ASC

-- 聚合函数
-- COUNT 计数
SELECT COUNT(*) AS 饭卡数
FROM Table_Card
-- DISTINCT
SELECT COUNT(DISTINCT School) AS 院系数目
FROM Table_Student
-- 求和,求平均函数
SELECT AVG(Balance) AS 平均余额,SUM(Balance) AS 总余额
FROM Table_Card
-- 求最大最小
SELECT MAX(payamount) AS 最多消费,MIN(payamount) AS 最少消费
FROM Table_Salebill
WHERE saledate='2021-07-06'


-- GROUP BY 与 HAVING 子句
-- 用过了 GROUP BY 就不能再执行 WHERE 了,需要使用 HAVING 来筛选
SELECT School AS 学院名称,COUNT(*) AS 学生数  
FROM Table_Student 
GROUP BY School
HAVING COUNT(*)>2;


