/* 
    解析器在调用函数每次都会向函数内部传递进一个隐含的参数
        这个隐含的参数就是this,this指向的是一个对象
        这个对象我们称为函数执行的 上下文对象
        根据函数调用方式的不同,this会指向的值会不同
            1.以函数的形式调用时,this永远是window
                - 函数调用this,this就是window
            2.方法的形式调用时,this就是调用方法的对象
                - 谁调用this,谁就是this
*/

function fun3(){

    console.log(this);
}

fun3();

function fun2()
{
    console.log(this.name);
}

var obj = {
    name:"tom",
    sayName:fun2
};

console.log(obj);

obj.sayName();

/* 
    创建一个name变量,fun函数
 */

var name = "全局";

function fun() {
    console.log(this.name);
}

var obj = {
    name:"孙悟空",
    sayName:fun
}

var obj2={
    name:"沙和尚",
    sayName:fun
}

obj.sayName();
obj2.sayName();