
/* 
    使用 Number() 函数
        - 字符串
            1.如果是纯数字,则直接将其转换为数字
            2.如果有非数字的内容,则转化为 NaN
            3.如果为空或是空格,则转化为 0
        - Boolean值
            true变 1,false变 0
        - Null值
            null变 0
        - Undefined值
            undefined变 NaN
*/

var a = "123";
a = Number(a);
console.log(a);
console.log(typeof a);

var a = "123试试";
a = Number(a);
console.log(a);
console.log(typeof a);

/* 
    parseInt() 
        把一个字符串转化为整数
        读出整数,其他去除,可以用于取整
        加上逗号后面可以写进制
    parseFloat()
        把一个字符串转化为浮点数

    对非 String使用 parseInt或 parseFloat
    则会转换为 String再操作
*/

a="123.456px";
a=parseInt(a,8);
console.log(typeof a);
console.log(a);

a="123.456px";
a=parseFloat(a);
console.log(typeof a);
console.log(a);