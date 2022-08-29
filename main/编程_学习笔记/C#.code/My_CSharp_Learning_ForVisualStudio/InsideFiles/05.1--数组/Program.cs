using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _05._1__数组
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            
            - 数组声明

                数据类型[空] 数组名;

                数据类型[空] 数组名 = {数值1, 数值2, ...};

            - 索引
                
                数组名[索引]
                
            */

            int[] height;
            int[] ages = { 12, 12, 54, 45, 13 };

            Console.WriteLine(ages[2]);
            Console.ReadKey();

            /*
                
            - 数组赋值

                数据类型[空] 数组名;  //声明

                1. 数组名 = new 数据类型[长度];  // 此时申请内存,赋值为默认值

                2. 数组名 = new 数据类型[空/长度]{数值1, 数值2, ...};   
            */

            int[] weight;
            weight = new int[10]; // 默认值为 0 

            double[] eyesight;
            eyesight = new double[] { 5.1, 5.2, 4.8 };

            Console.WriteLine(weight[2]);
            Console.ReadKey();

            //最常用(写到一行)
            int[] array=new int[] { 1,2,3,4};

            /*
            
            - 遍历数组
                
                for循环  while循环 

                foreach 循环

                    foreach(数据类型 临时变量 in 数组)
                    {
                        ...
                    }


            - 数组长度属性
                数组名.Length
            */

            for (int i = 0; i < 5; i++)
            {
                Console.Write(ages[i]+" ");
            }

            Console.ReadKey();


            Console.Write("\n"+ages.Length+"\n");

            // foreach 循环用法,像 Python 的 for in
            foreach(int temp in ages)
            {
                Console.Write(temp + " ");
            }

            Console.ReadKey();

        }
    }
}
