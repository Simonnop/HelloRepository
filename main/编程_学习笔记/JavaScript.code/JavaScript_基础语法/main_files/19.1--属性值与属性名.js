
var obj = new Object();

/* 
    属性名:
        不强制要求遵守规范,但要尽量遵守规范

    如果使用特殊的属性名,不能采用 . 的方式来操作
        需要使用另一种方式:
            对象["属性名"] = 属性值;
        
        这种方式更为灵活,这样变量值是多少就会读取那个属性      
*/

obj.var="sdha";
console.log(obj.var);

obj["shisdx.jfojao153"] = "zhe";
console.log(obj["shisdx.jfojao153"]);

var a = "var";
console.log(obj.a);
console.log(obj[a]);

/* 
    属性值:
        可以是任意的数据类型
        也可以是一个对象
*/

var obj2 = new Object();
obj2.name = "Tim";
obj2.age = 18;

obj["obj2"]=obj2;

console.log(obj);
console.log(obj2)

/* 
    in 运算符
        - 通过该运算符可以检查一个对象是否含有指定属性
        - 语法:
            "属性名" in 对象
        - 返回 Boolean
*/

console.log("name" in obj2);
