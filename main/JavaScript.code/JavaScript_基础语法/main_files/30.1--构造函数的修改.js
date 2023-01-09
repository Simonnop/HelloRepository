/* 
    创建一个Person构造函数
*/

function Person(name,age,gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.sayName = function(){
        console.log("Hello大家好，我是："+this.name);
    };
}

/* 
    创建一个Person的实例
*/

var per1 = new Person("孙悟空",18,"男");
var per2 = new Person("猪八戒",23,"男");

per1.sayName();
per2.sayName();

/* 
    sayName目前是在内部创建的
    也就是构造函数每执行一次就会创建一个新的sayName方法
    也就是所有实例的sayName都是唯一的
    这是完全没有必要的,可以共享
*/

/* 
    将sayName方法在全局作用域中定义

    将函数定义在全局作用域中,污染了全局作用域的命名空间,也不安全
*/

function sayHello(){
    console.log(this.name)
}

function CreatePerson(name,age,gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
    this.sayName = sayHello;
}

var p3 = new CreatePerson("tom",23,"male");

sayHello(p3);
console.log(p3);









