/* 
    定义一个求两个数和的函数
        可以在函数中的()中来指定一个或多个形参
        多个形参之间使用 逗号 隔开
        声明形参就相当于在函数内部声明了对应的变量但是并不赋值

    - 调用函数时不会检查实参的类型,可能获得非法的参数,需要进行类型检查
    - 实参的数量少于形参的数量,则会被定义为 undefined
    - 实参可以是任意的数据类型
*/

function sum(a,b) {

    console.log(a+b);
    
}

sum(1,5);

/* 
    参数可以传对象,也可传函数
*/

var obj = {
    name:"孙悟空",
    age:18,
    gender:"男",
    address:"花果山"
}

function Hello(obj) {
    console.log(
        "大家好,我是"+obj.name+",我今年"+obj.age+"岁了,我是一个"+obj.gender+"的,住在"+obj.address);
    
}

Hello(obj);