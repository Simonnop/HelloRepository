/* 
    原型 prototype

    我们所创建的每一个函数，解析器都会向函数中添加一个属性 prototype
        这个属性对应着一个对象，这个对象就是原型对象
        
    如果函数作为普通函数调用 prototype，没有任何作用
    如果函数作为构造函数调用，他所创建的对象都有一个隐含属性
        指向该构造函数的原型对象，我们可以通过__proto__来访问该属性
    
    原型对象就相当于一个公共的区域，所有通过一个类的实例都可以访问到这个原型对象
        我们可以将对象中共有的属性，同意设置到原型对象中

    当我们访问对象的一个属性或方法时,他会现在自身中寻找,没有则会去 prototype中找
*/

function Person() {

}

var p = new Person();
Person.prototype.a = "123";

console.log(Person.prototype);
console.log(p.__proto__);
console.log(p.a);

/* 
    将方法写入函数
        - 向原型中添加sayName方法
*/

function CreatePerson(name,age,gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
}

CreatePerson.prototype.sayHello = function () {
    console.log(this.name);
};

var per = new CreatePerson("me",18,"i");

per.sayHello();

/* 
    创建一个构造函数
*/

function MyClass(){

}

MyClass.prototype.name = "me";

var mc = new MyClass();

console.log(mc.name);

/* 
    查看对象自身存在的属性:
        对象名.hasOwnProperty("属性名")
*/

console.log(mc.hasOwnProperty("name"));

/* 
    原型对象也是对象,所以它也有原型
        当我们使用一个对象的属性或方法时,会先在自身中寻找
            自身如果有,则直接使用
            如果没有则去原型对象中寻找,如果原型对象中有,则使用
            如果没有则去原型的原型中寻找,直到找到Object对象的原型
            Object对象的原型没有原型,如果在Object中依然没有找到,则返回Undefined
        以上就是 - 原型链
*/