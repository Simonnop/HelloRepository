insert into Table_S values('12345671','Tim','M',18,'管理学院');
insert into Table_S values('12345672','Tom','M',18,'管理学院');
insert into Table_S values('12345673','Jack','M',18,'管理学院');
insert into Table_S values('12345674','Sam','M',18,'管理学院');

insert into Table_C values('76543211','数据库1','无',5.5);
insert into Table_C values('76543212','数据库2','无',5.5);
insert into Table_C values('76543213','数据库3','无',5.5);

insert into Table_SC values('100','12345671','76543211');
insert into Table_SC values('101','12345671','76543212');
insert into Table_SC values('102','12345671','76543213');

insert into Table_SC values('102','12345672','76543211');
insert into Table_SC values('101','12345672','76543212');
insert into Table_SC values('100','12345672','76543213');

insert into Table_SC values('101','12345673','76543211');
insert into Table_SC values('102','12345673','76543212');
insert into Table_SC values('100','12345673','76543213');

insert into Table_SC values('101','12345674','76543211');
insert into Table_SC values('100','12345674','76543212');
insert into Table_SC values('102','12345674','76543213');