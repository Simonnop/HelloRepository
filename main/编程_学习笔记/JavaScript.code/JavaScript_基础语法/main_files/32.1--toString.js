/* 

*/

function Person(name,age,gender){
    this.name = name;
    this.age = age;
    this.gender = gender;
}

var per = new Person("孙悟空",18,"男");

/* 

    当我们直接在页面中打印一个对象时，实际上输出的是对象的toString()方法的返回值
    
    (目前自己没有遇到)
    如果我们希望在输出对象时不输出[object Object],可以为对象添加一个toString()方法

    这个toString位于原型的原型的 Object
*/

Person.prototype.toString = function(){
    console.log("Person { name: "+this.name+", age: "+this.age+"}")
} 

console.log(per);

per.toString();

