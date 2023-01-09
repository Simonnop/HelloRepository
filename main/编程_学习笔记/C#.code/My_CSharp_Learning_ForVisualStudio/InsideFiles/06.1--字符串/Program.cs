using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06._1__字符串
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string name = "Micheal";
            name = "" + 45; // "45"
            name = "Michael" + "123"; // "Michael123"

            /*
            
            字符串
            
            字符串是一串字符
            在程序中,一个字符串可以当作一个字符数组

            str.Length 取得字符串长度

            */

            Console.WriteLine(name.Length);
            Console.WriteLine(name[2]);

            Console.ReadKey();

            /*
            
            常用方法

            都有返回值,需要变量接收

            小写  .toLower() 
            大写  .toUpper() 
            
            去空格  .Trim() 
            去前面的空格  .TrimStart()
            去后面的空格  .TrimEnd()

            
            分割方法 .Split( 分隔的char )

            */

            name = "Hello World";
            string names = "Tim,Sam,Mike";

            string[] strNames = names.Split(',');

            foreach(string hisName in strNames)
            {
                Console.WriteLine(hisName);
            }

            Console.ReadKey();
        }
    }
}
