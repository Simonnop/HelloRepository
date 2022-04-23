
CREATE DATABASE CARD2022;
USE CARD2022;

CREATE TABLE Table_Card (
    CardID char(8)  PRIMARY KEY,
    Password varchar(8) NOT NULL,
    Balance money  NOT NULL CHECK (Balance>=0 ),
 	State char(1)  NOT NULL CHECK (State in ('0','1','2')));


CREATE TABLE Table_Student (
StudentID char (12) NOT NULL,
CardID char(8),
Sname varchar(8) ,
Sex char(1)  CHECK ( Sex in ('M','F')),
School varchar(20)  NOT NULL,
PRIMARY KEY (StudentID),
FOREIGN KEY (CardID) REFERENCES Table_Card(CardID));


CREATE TABLE Table_Machine (
MachineID char(8) PRIMARY KEY ,
State char(1),
Address varchar(20));

CREATE TABLE Table_Salebill (
number int PRIMARY KEY IDENTITY(1,1),
CardID char(8) NOT NULL,
MachineID char(8) NOT NULL,
payamount decimal(10,2) NOT NULL,
saledate date NOT NULL,
CONSTRAINT "salebill_CIDfk" FOREIGN KEY (CardID) REFERENCES Table_Card(CardID) ON DELETE CASCADE ,
FOREIGN KEY (MachineID) REFERENCES Table_Machine(MachineID) ON DELETE CASCADE);

 
INSERT INTO Table_Card VALUES('C00001','135', 500,'0');
INSERT INTO Table_Card VALUES('C00002','459', 86.5,'1');
INSERT INTO Table_Card VALUES('C00003','123456', 32,'2');
INSERT INTO Table_Card VALUES('C00004','888', 107.6,'1');
INSERT INTO Table_Card VALUES('C00005','159', 145,'0');
INSERT INTO Table_Card VALUES('C00006','123321', 800,'0');
INSERT INTO Table_Card VALUES('C00007','666666', 12,'2');
INSERT INTO Table_Card VALUES('C00008','1111', 209,'0');
INSERT INTO Table_Card VALUES('C00009','123', 58.2,'0');
INSERT INTO Table_Card VALUES('C00010','12_456', 400,'0');
INSERT INTO Table_Card VALUES('C00011','12%12', 500,'0');


INSERT INTO Table_Student  VALUES ('201901010001','C00001','张伟','M', '管理学院');
INSERT INTO Table_Student  VALUES ('201901010002','C00002','周萍','F' ,'管理学院');
INSERT INTO Table_Student  VALUES ('201901010003','C00003','孙琦','M' ,'管理学院');
INSERT INTO Table_Student  VALUES ('201901010004','C00004','李子欣','F', '管理学院');
INSERT INTO Table_Student  VALUES ('20190201001','C00005','陈亮','M', '机械学院');
INSERT INTO Table_Student  VALUES ('20190201002','C00006','赵榕','F', '机械学院');
INSERT INTO Table_Student  VALUES ('20200301001','C00007','黄磊','M', '经济学院');
INSERT INTO Table_Student  VALUES ('202003010002','C00008','刘杰','M', '经济学院');
INSERT INTO Table_Student  VALUES ('202003010003','C00009','刘杰','M', '计算机学院');
INSERT INTO Table_Student  VALUES ('202003010004',null ,'张萌','M', '经济学院');
INSERT INTO Table_Student  VALUES ('202003010005',null ,'张子新','M', '计算机学院');
INSERT INTO Table_Student (StudentID, School)  VALUES ('2021024921', '管理学院');



INSERT INTO Table_Machine VALUES('00000011',0,'第一食堂');
INSERT INTO Table_Machine VALUES('00000012',0,'第一食堂');
INSERT INTO Table_Machine VALUES('00000013',1,'第一食堂');
INSERT INTO Table_Machine VALUES('00000021',0, '第二食堂');
INSERT INTO Table_Machine VALUES('00000022',0,'第二食堂');
INSERT INTO Table_Machine VALUES('00000023',1, '第二食堂');
INSERT INTO Table_Machine VALUES('00000031',0,'第三食堂');
INSERT INTO Table_Machine VALUES('00000032',0, '第三食堂');


INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00005', '00000011',13,'2021-5-10');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00004', '00000011',8,'2021-5-10');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate)  VALUES( 'C00001', '00000011',10.5,'2021-5-26');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00004', '00000023',25,'2021-5-28');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00001', '00000012',20,'2021-5-30');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00004', '00000022',16,'2021-6-01');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00003', '00000031',8.9,'2021-6-29');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00001', '00000022',9,'2021-7-2');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00005', '00000023',21,'2021-7-3');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00001', '00000023',32, '2021-7-4');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00001', '00000031',56, '2021-7-4');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00001', '00000013',1, '2021-7-5');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00001', '00000021',21, '2021-7-5');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00006', '00000023',380, '2021-7-6');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00008', '00000012',15, '2021-7-6');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00005', '00000012',15,'2021-7-6');
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES( 'C00003', '00000012',15,'2021-7-6');

