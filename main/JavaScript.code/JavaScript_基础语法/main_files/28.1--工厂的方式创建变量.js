/* 
    使用工厂方法创建对象
        通过该方法可以大批量地创建对象
*/

function createPerson(name,age,gender){
    
    var obj = new Object();

    obj.name=name;
    obj.age=age;
    obj.gender=gender;
    obj.sayName = function(){
        console.log(this.name)
    }

    return obj;
}

var obj2 = createPerson("沙和尚",18,"男");
var obj3 = createPerson("孙悟空",23,"男");

console.log(obj2);
console.log(obj3);

/* 
    使用工厂的方法创建的对象,使用的构造函数都是Object
        所以创建的对象都是Object这个类型
        这就导致我们无法区分出多种不同的对象
*/

