
var str2 = 'hello';



console.log(str2);

/* 
    在JS中所有的数值都是Number类型
        包括整数与浮点数(小数)

    JS进行浮点运算,可能得到一个不精确的结果
    千万不要使用JS进行精确度高的运算

    JS中 Number可以表示的最大值:
        1.7976931348623157e+308
    超过最大值,返回 Infinity,是个字面量

    大于零的最小值:
        5e-324  

    NaN (Not a Number)也是一个数字
*/

var a = "123";

a = Infinity;

/*
    typeof 检查变量的类型
        语法: typeof 变量

    检查字符串时,结果为 string
    检查数字时,结果为 number
*/

console.log(Number.MAX_VALUE);
console.log(Number.MIN_VALUE);

console.log(typeof a);
