using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _02._1__基本语法
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Console.Write("Hello ");
            Console.Write("World\n");

            /*
             *  - 输出
             *  
             *      Console.Write 一直在一行中写
             *      Console.WriteLine 写完一个语句换行
             *  
             *      取消转义字符,用 @
             *          @"....."
             *          
             *          
             *  - 变量声明
             *  
             *      int,double,char,string 与 C 相同 
             *      
             *  - 强制类型转换
             *  
             *      a = (type)b;
             *          
             *  - 字符串的拼接: + 加号
             *  
             *      字符串1 + 字符串2
             *         字符串 + 其他类型 : 强制转化为字符串
             *      
             *  
             *  - 读取
             *  
             *      String str = Console.ReadLine()
             *          默认读取类型为字符串
             *      
             *      数字:
             *          字符串数字转化为 int
             *          int num = Convert.ToInt32(str)                 
             *          
             *          int a = Console.ReadLine()
             *          
             *          String str = Console.ReadLine();
             *          int strInt = Convert.ToInt32(str);
             *          Console.WriteLine(strInt+ "-");
             *
             *      合并写法(常用)
             *          int a = Convert.ToInt32(Console.ReadLine());
             *
             *      
             */
            Console.Write("请输入a的值:");
            int a = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(a + "-\n");

            Console.ReadKey();

            //读取一个字符

            Console.Write("enter a char: ");
            char c = (char)Console.Read();

            Console.WriteLine(c);

            Console.ReadKey();

            /* 
             *  - 字符串格式化输出
             *      使用大括号 {n} 来指定值的输出
             *      Console.WriteLine("{0}+{1}={2}",a,b,a+b)
             */

            int b;
            a = 1; b = 3;
            Console.WriteLine("{0}+{1}={2}", a, b, a + b);
            Console.WriteLine("{0}+{0}={1}", a, a + a);

            Console.ReadKey();

            /*
             *  - 数学运算符
             *      + - * / % ++ --
             *      与 C 一样
             *      
             *  - 关系运算符
             *      bool a = true;
             *      bool b = false;
             *  
             *      == > < >= <= != 
             *      与 C 一样
             *      
             *      bool a = 5 == 4;
             */

            bool d = 7 <= 8;
            Console.WriteLine(d);

            Console.ReadKey();

            /*
             *  - 逻辑运算符
             *      || 或
             *      && 与
             *      !  非
             *      与 C 相同
             */
        }
    }
}
