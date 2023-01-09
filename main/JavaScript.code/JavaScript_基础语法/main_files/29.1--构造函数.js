/* 
    使用工厂的方法创建的对象,使用的构造函数都是Object
        所以创建的对象都是Object这个类型
        这就导致我们无法区分出多种不同的对象
*/

/* 
    创建一个构造函数,专门用来创建Person对象的
        构造函数就是一个普通的函数,创建的方式与普通函数没有区别
        不同的是构造函数的首字母大写

    构造函数与普通函数的区别是调用方式不同
        普通函数直接调用,而构造函数需要使用new关键字来调用

    构造函数的执行流程:
        1.立刻创建一个新的对象
        2.将新建的对象设置为函数中的this,在构造函数中可以使用this来引用新建的对象
        3.逐行执行函数中的代码
        4.将新建的对象作为返回值返回
*/

function Person(){
    this.name="孙悟空";
    this.age=18;
    this.gender="男";
    // 没有 return
}

var per = new Person();

/* 
    此时的 this就是 per
*/

console.log(per);

function CreatePerson(name,age,gender){
    this.name=name;
    this.age=age;
    this.gender=gender;
}

var p1=new CreatePerson("孙悟空",18,"男");
var p2=new CreatePerson("猪八戒",78,"男");

console.log(p1);
console.log(p2);

/* 
    使用同一个构造函数创建的对象,我们称为一类对象,也将一个构造函数称为一个类
        我们将通过一个构造函数创建的对象,称为是该类的实例

    使用 instanceof函数 可以检查对象是否是一个类的实例
        语法:
            对象 instanceof 构造函数
            - 返回值为 Boolean

    所有的对象都是Object的后代
*/

console.log(p1 instanceof Person);
console.log(per instanceof Person);

console.log(p1 instanceof Object);
console.log(per instanceof Object);

/* 
    this的情况
        1.函数调用 - window
        2.方法调用 - 方法对象自己
        3.构造函数调用 - 新创建的对象
*/
