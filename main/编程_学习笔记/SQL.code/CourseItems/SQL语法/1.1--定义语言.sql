create table Student_Info
(
	StuID char(8),
	StuName varchar(10) not null,
	Sex char(6) check (Sex in ('male','female')),
	School varchar(20) not null,
	PRIMARY KEY(StuID)
);


-- 数据库创建 (master中)
create database 数据库名

-- 数据库的撤销 (master中)
drop database 数据库名

-- 对数据库进行操作 (master中)
USE 数据库名


-- 创建表
CREATE TABLE 表名
(
	--	<属性名>　<数据结构>　[约束],
	Element1 varchar(10) not null,
	Element2 char(4) check (Element2 in ('值1','值2')),
);

-- 约束:实体完整性约束,参照性约束

-- varchar(8) 与 char(8)
-- 都可以填 8个以内的字符,但 char(8)开辟的内存空间是一定的