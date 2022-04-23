var obj = {
    name:"tom",
    age:18,
    gender:"男"
};

/* 
    枚举对象中的属性
    使用 for ... in 语句

    语法:
        for(var 变量 in 对象){
            语句
        }

    有几个循环体就循环几次
    每次执行时会把属性名赋值给变量
*/

for (var n in obj) {
    
    console.log(n);
    console.log(obj[n]);

    console.log(n+":"+obj[n]);
}
