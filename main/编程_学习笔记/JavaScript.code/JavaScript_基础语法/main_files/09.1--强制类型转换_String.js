/* 
    强制类型转换
        - 指将一个数据类型转换为其他的数据类型
        - 类型转换主要指,将其他的数据类型转换为 String Number Boolean
*/

/* 
    转换为 String
        1.调用被转换数据类型的 toString() 方法
            xxx.yyy()
            该方法不会影响到原变量,会将转换的结果返回
            注意: null与 undefined没有 toString方法,会报错
    
        2.调用 String() 函数
            将被转换的数据作为参数
            注意: 对于 Number和 Boolean,实际用的就是 toString
                  但对于 null,则直接转换为 "null";对于 undefined,则直接转换为 "undefined"
*/

var a = 123;
a = a.toString();
console.log(a);
console.log(typeof a);

var b = 123;
b = String(b);
console.log(b);
console.log(typeof b);
