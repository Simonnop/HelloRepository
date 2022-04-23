/* 
    slice()
        - 从选定的数组中提取指定的元素
        - 参数:
            1.截取开始的位置索引,包含自身
            2.截取结束的位置索引,不包含自身(可以不写,就截取到末尾)
        - 该方法不会改变原数组,而是会封装到新数组
        - 索引可以传递一个负值,就是从末尾往前数
*/

var arr = ["孙悟空", "猪八戒", "沙和尚"];

var result = arr.slice(1,3);
var result2 = arr.slice(1);

console.log(arr);
console.log(result);
console.log(result2);

/* 
    splice()
        - 删除数组中的指定元素
        - 会影响到原数组
        - 参数:
            1.截取开始的位置索引,包含自身
            2.截取的数量(写零就不删除)
            3.第三个及以后,设置元素,会插入索引位置的前面
        - 返回值为删除的值,会封装到新数组
*/

var result3 = arr.splice(1,1,"牛魔王","红孩儿");
console.log(arr);
console.log(result3);

// 只添加
var result4 = arr.splice(1,0,"二郎神");
console.log(arr);
console.log(result3);