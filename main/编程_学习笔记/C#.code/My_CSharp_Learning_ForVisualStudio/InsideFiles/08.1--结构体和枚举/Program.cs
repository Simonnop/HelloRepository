using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _08._1__结构体和枚举
{
    //  枚举类型: 限制变量的可能性
    //  默认以 0,1,2,... 赋值 
    enum Days { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday }
    internal class Program
    {
        //  结构体类型
        struct Person
        {
            public int age;   // 对外可见
            private string name;   // 对外不可见
            internal string fname;  // 命名空间内可访问
            //protected string astName;  //继承才可以访问
        

        static void Main(string[] args)
        {
            // 结构体的调用
            Person person1 = new Person();
            person1.age = 10;
            Console.WriteLine(person1.age);
            Console.WriteLine(Days.Monday);

            Console.ReadKey();


        }

    }
}
