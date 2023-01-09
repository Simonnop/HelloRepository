using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _04._1__基本数据结构
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            
            类型全览
                bool	布尔值	                True 或 False	                            False
                byte	8 位无符号整数	        0 到 255	                                0
                char	16 位 Unicode 字符	    U +0000 到 U +ffff	                        '\0'
                decimal	128 位精确的十进制值    (-7.9 x 1028 到 7.9 x 1028) / 100 到 28	    0.0M
                double	64 位双精度浮点型	    (+/-)5.0 x 10-324 到 (+/-)1.7 x 10308	    0.0D
                float	32 位单精度浮点型	    -3.4 x 1038 到 + 3.4 x 1038	                0.0F
                int	    32 位有符号整数类型	    -2,147,483,648 到 2,147,483,647	            0
                long	64 位有符号整数类型	    到 9,223,372,036,854,775,807	            0L
                sbyte	8 位有符号整数类型	    -128 到 127	                                0
                short	16 位有符号整数类型	    -32,768 到 32,767	                        0
                uint	32 位无符号整数类型	    0 到 4,294,967,295	                        0
                ulong	64 位无符号整数类型	    0 到 18,446,744,073,709,551,615	            0
                ushort	16 位无符号整数类型	    0 到 65,535	                                0

            浮点型
                float   单精度  声明时要加上 f
                double  双精度  声明小数时默认

            */

            float a = 4.5f;
            double b = 2.1;
            Console.WriteLine("{0} and {1}",a,b);

            Console.ReadKey();

            /*
                类型转化
                    编译器只检测容器大小,不检查变量具体大小
            */

            //隐式转换
            byte c = 32;
            int d = 100;
            d = c;

            //显式转换
            c = (byte)d;
            int e = Convert.ToInt32("2234");
            string f = "4156" + 12;
            string g = Convert.ToString(123);

        }
    }
}
