/* 
    创建对象的简单方式

    可以在创建对象时直接添加属性
        语法: {属性名:属性值,属性名:属性值....}

    属性名若特殊,则需加上引号

    属性名与属性值是一组一组的名值对结构
*/

var obj={

    name:"hello",
    age:18,
    gender:"男",

    test:{name:"猪八戒"}

};

obj.name="123";

console.log(obj);