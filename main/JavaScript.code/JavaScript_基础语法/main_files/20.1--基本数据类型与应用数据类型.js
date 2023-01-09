/* 
    基本数据类型
        - 值保存在栈内存中
        - 值与值之间是独立存在的
*/

var a = 1;
var b = a;

a = 2;

console.log(a);
console.log(b);

/* 
    引用数据类型(对象)
        - 值保存在堆内存中
        - 每创建一个新的对象,都会在堆内存中开辟一个空间
        - 对象的值实际是保存的一个地址

        值与值之间存在联系,修改会改变内存中的值,故会产生影响
*/

var obj1 = new Object();
obj1.name = "猪八戒";

var obj2 = obj1;

obj1.name = "孙悟空";

console.log(obj1);
console.log(obj2);

/* 
    设置 obj2 = null
    
    obj1 不受影响
        因为设置时断开了连接
*/

obj2 = null;

console.log(obj1);
console.log(obj2);

/* 
    对象之间的比较,是地址值的比较
*/

 obj1.name = "1";
 
 var obj3=new Object();
 obj3.name = "1";

console.log(obj1);
console.log(obj3);

console.log(obj3 == obj1);
