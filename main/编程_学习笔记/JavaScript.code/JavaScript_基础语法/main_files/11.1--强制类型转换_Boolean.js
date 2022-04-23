/* 

    Boolean() 函数
        - 数字:
            除了0和null,其他都是true
        - 字符串:
            只要有东西(包括空格),就是true
        - Null:
            null变 false
        - Undefined:
            undefined变 false
            
        - 对象也会转换为 true

*/

var a=123;
a=Boolean(a);
console.log(a);

var a=-123;
a=Boolean(a);
console.log(a);

var a=0;
a=Boolean(a);
console.log(a);