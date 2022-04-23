
var arr = ["孙悟空", "猪八戒", "沙和尚"];

var arr2 = ["孙悟空", "沙和尚"];

/* 
    concat()
        - 可以连接多个数组,产生新的数组返回
        - 对原数组不会产生影响
*/

var result = arr.concat(arr2);

console.log(result);

/* 
    join()
        - 该方法可以将数组转化为一个字符串
        - 不会对原数组产生影响,产生字符串进行返回
        - 参数:元素的连接符(不指定默认逗号,不想要就设置 "(空)" )
*/

result = arr.join("~");

console.log(result);

/* 
    reverse()
        - 反转数组
        - 会直接修改原数组
*/

arr.reverse();

console.log(arr);

/* 
    sort()
        - 数组中的元素进行排序
        - 会影响原数组
        - 排序依据: Unicode编码(数字也是)

        - 可以在参数指定回调函数,来指定排序规则
            若回调函数返回一个大于0的值,则会交换位置
*/

arr.sort();

console.log(arr);

arr2 = [1,3,2,9,5,6,4];


//数字排序
arr2.sort(function(a,b){
    return a-b;
})

console.log(arr2);

