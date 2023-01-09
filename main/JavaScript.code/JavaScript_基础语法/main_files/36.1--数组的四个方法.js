/* 

*/

var arr = ["孙悟空", "猪八戒", "沙和尚"];

console.log(arr);

/* 
    push()
        - 该方法可以在数组末尾添加一个或多个元素,并返回数组的新长度
        - 要添加的元素作为参数传递,自动添加到末尾
*/

var result = arr.push("唐僧","白骨精");

console.log(arr);

console.log(result);

/* 
    pop()
        - 删除数组的最后一个元素,并将其作为返回值
*/

result = arr.pop();

console.log(arr);

console.log(result);

/* 
    unshift()
        - 向数组开头添加一个或多个元素,并返回数组的新长度
*/

result = arr.unshift("牛魔王","二郎神");

console.log(arr);

console.log(result);

/* 
    shift()
        - 删除数组的第一个元素,并将其作为返回值
*/

result = arr.shift();

console.log(arr);

console.log(result);

