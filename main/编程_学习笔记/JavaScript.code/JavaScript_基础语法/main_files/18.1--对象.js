/* 
    六种数据类型
    - String
    - Number
    - Boolean
    - Null
    - Undefined
        只要不是上边的五种,就是对象

    使用基本数据类型的数据,都是独立的,不能成为一个整体

    - Object 对象
        属于一种复合的数据类型,可以保存多个不同的数据类型的属性

    对象的分类
        1.内建对象
            - 由 ES标准中定义的对象,在任何的 ES中都可以是实现
            - 如: Math String Number Boolean Function Object...
        2.宿主对象
            - 由 JS的运行环境提供的对象，由浏览器提供
            - 如: BOM DOM
        3.自定义对象
            - 由开发人员自己创建的对象
        
*/

/* 
    创建对象

    使用 new关键字调用的函数,是构造函数 constructer
        构造函数是专门用来创建对象的函数
*/

var obj = new Object();

console.log(typeof obj);

/* 
    向对象中添加属性 / 更改属性
        语法:
            对象.属性名 = 属性值;

*/

obj.name = "孙悟空";
obj.gender = "男";
obj.age = 18;

console.log(obj);

obj.name = "Tom";

console.log(obj);

/* 
    读取对象中的属性
        语法:
            对象.属性名

    如果读取对象中没有的属性,则不会报错,而会返回 Undefined
*/

console.log(obj.name);

/* 
    删除对象的属性
        语法: delete 对象.属性名
*/

delete obj.age;

console.log(obj);






