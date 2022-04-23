/* 
    数组  Array
        - 数组它也是一个对象
        - 数组使用数字来作为索引
        - 索引  Index
            从零开始的整数就是索引
        - 数组的存储性能比普通对象要好
*/

var arr = new Array();

// typeof检查一个数组,会返回 Object

console.log(typeof arr);

/*
    向数组中添加元素
    语法:
        数组[索引] = 值
*/

arr[0] = 10;
arr[1] = 22;
arr[2] = 33;

/* 
    读取数组中的元素
    语法: 数组[索引]
        如果读取不存在的索引,返回 undefined
*/


console.log(arr[2]);

/* 
    获取数组长度
        数组.length
    获得最大的索引+1
*/

console.log(arr.length);

arr.length=2;

console.log(arr);

arr.length=4;

console.log(arr);

/* 
    向数组中的最后一个位置添加元素
*/

arr[arr.length]=23;

console.log(arr);