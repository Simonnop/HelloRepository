using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// .sln      解决方案文件,里面包含整个解决方案的信息,可以双击打开
// .csproj   项目文件,里面包含着整个项目的信息.可以双击打开

namespace _01._1__文件结构  
    // 项目名称  大括号内为命名空间范围
{
    internal class Program
    // 类名称  大括号内为内范围
    {
        static void Main(string[] args)
        // 方法或者函数
        // Main函数是程序的主入口,代码若想被执行,则需写在Main函数内
        {
            // 每行代码以分号为结尾

            Console.WriteLine("Hello World");

            // 程序暂停，按下任意键继续，显示在控制台中
            Console.ReadKey();

            Console.WriteLine("我也是Hello World");

            // 程序暂停
            Console.ReadKey();
        }

    }
}


// 按下 Ctrl+Shift+B 生成解决方案：可以用于检查错误
