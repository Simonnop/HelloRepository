/* 
    创建一个对象
*/

var obj = {
    name:"孙悟空",
    age:18,
    sayName:function(){}
}

/* 
    对象的属性值也可以是一个函数

    调用函数叫做调用这个对象的方法
*/

obj.sayName = function () {
    console.log(obj.name);
};

obj.sayName();

