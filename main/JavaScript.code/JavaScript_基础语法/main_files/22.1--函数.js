/*
    函数
        - 函数也是一个对象
        - 函数中可以封装一些功能(代码),在需要时可以执行这些功能(代码)
        - 函数中可以保存一些代码,在需要时调用

    创建函数对象
        - 语法: var 函数名 = new Function();

        - 我们很少使用构造函数来创建一个函数,多使用函数声明
        - 函数声明: function 函数名([形参1,形参2...]){语句...}

        - 封装到函数中的代码不会立即执行,调用时才会执行

    调用函数
        - 语法: 函数名();

 */

{
    //代码块
    console.log("第1行");
    console.log("第2行");
    console.log("第3行");
}

var fun = new Function("console.log('这是我的第一个函数');");

console.log(typeof fun);

fun();



// 常用 - 函数声明: function 函数名([形参1,形参2...]){语句...}

function fun2() {
    console.log("第1行");
    console.log("第2行");
    console.log("第3行");
}

fun2();

/* 
    使用 函数表达式 来创建函数
    var 函数名 = function([形参1,形参2...]){语句...};
*/

var fun3 = function(){
    console.log("第1行");
    console.log("第2行");
    console.log("第3行");
};

fun3();

/* 
    立即执行函数: (function(形参){语句})(传入的实参));
        函数被定义完,立即被调用,这种函数叫做立即执行函数
        立即执行函数只会执行一次
*/

(function(a,b){
    console.log(a+b);
    console.log("我是立即执行函数");
})(1,2);