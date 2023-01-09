/* 
    可以为循环语句创建一个 label,来标识当前的循环

    label:循环语句
        - 使用   break 语句名;  可结束指定循环

    continue:跳过当次循环
*/

outer:
for (let i = 0; i < 5; i++) {
    
    console.log("@外层循环"+i);
    
    for (let j = 0; j < 5; j++) {

        if (i==1) 
        {
            continue;    
        }
        
        if(i==2)
        {
            break outer;
        }

        console.log("内层循环"+j);
        
    }
    
}