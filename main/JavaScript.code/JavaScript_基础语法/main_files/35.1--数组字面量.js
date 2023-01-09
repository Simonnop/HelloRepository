/* 
    使用字面量创建数组时,可以直接指定元素
*/

var arr = [1,2,3,4,5,10];
console.log(arr);
console.log(arr.length);
console.log(arr[4]);

var arr2 = new Array(1,2,3,4);
console.log(arr2);

// 创建一个数组,数组中只有一个元素 10
arr = [10];
console.log(arr);

// 创建一个长度为 10的数组(少用)
arr2 = new Array(10);
console.log(arr2);

/* 
    数组中的数据可以是任意的类型

    也可以是对象,函数,数组,中间用 逗号 隔开即可
*/

var obj = {name:"孙悟空"};
arr[arr.length]=obj;

console.log(arr[arr.length-1].name);