/* 
    Null的值只有一个,就是 null
        专门用来表示为空的对象
        使用 typeof检查一个 null,返回 object

    Undefined的值也只有一个,就是 undefined
        声明一个变量但不给他赋值时, 它就是 undefined
*/

var a = null;

var b;

console.log(typeof a);

console.log("\n", typeof b);
