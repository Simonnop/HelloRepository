using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _07._1__函数_方法_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine();

            /*
                函数的定义

                    可以定义在main的上面或下面

                    函数类型 返回值类型 函数名(参数类型 参数){...}
                    static void CheakUserName(string name){...}

                函数的调用

                    函数名(参数);

                函数的重载
                
                    函数名相同的函数,会根据其参数来选择调用哪一个函数
                    常应用与多种数据结构的通用函数计算
            */

            CheakUserName("Tim");
            CheakUserName("Sam");

            bool result = Cheaker();
            Console.WriteLine(result);

            Console.ReadKey();

            // 普通数组,需要传入数组
            Console.WriteLine(AddNum(new int[] { 2, 4, 8 }));
            Console.ReadKey();
            // 参数数组,自动帮构建数组
            Console.WriteLine(NumAdder(2,4,6));
            Console.ReadKey();
        }

        static void CheakUserName(string name)
        {
            Console.WriteLine(name);
            Console.WriteLine("CHEAKED");

            Console.ReadKey();
        }

        static bool Cheaker()
        {
            return true;
        }

        // 参数也可以是数组,但是不好用

        static int AddNum(int[] array)
        {
            int sum = 0;
            foreach(int num in array)
            {
                sum += num;
            }
            return sum;
        }

        /*
            参数数组
                可以传递任意个个数的参数,自动帮我们构建数组
                参数数组前添加 params
                此参数必须是函数的最后一个参数
        */

        static int NumAdder(params int[] array)
        {
            int sum = 0;
            foreach (int num in array)
            {
                sum += num;
            }
            return sum;
        }
    }
}
