-- 2022.3.8

-- 选择特定项目输出数据
INSERT INTO Table_Card (CardID,Balance,Password,State) 
VALUES ('C00022',2000,'290%%22','0');


-- 插入来自其他表的数据到新表
INSERT INTO Table_Card2
-- 选择来自 Table_Card 的所有数据
SELECT * FROM Table_Card
-- 筛选 balance 大于等于 100 的列
WHERE balance>=100;


-- 删除表中的行
DELETE FROM Table_Salebill
-- WHERE 后写条件
WHERE CardID='C00001';


-- 单字段更新
UPDATE Table_Card
-- 给某项属性设定值
SET Balance=0
-- 选择符合条件的数据
WHERE State=2;


