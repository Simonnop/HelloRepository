using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _09._1__Class类
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var Person1 = new Person(10);
            Console.WriteLine(Person1.GetSuper());
            Console.WriteLine(Person1.Age);
            Person1.Age = 10;
            Console.ReadKey();
        }
    }

    
    class Person: ISuper  // 继承接口
    {
        int age;

        //  特殊方法的创建

        public int Age
        {
            get;
            set;
        }

        public Person(int myage)
        {
            this.age = myage;
        }

        public int GetSuper()
        {
            return age;
        }

        // static 静态方法,是类的方法,不能通过类调用
    }

    interface ISuper
    {
        // 接口
        int GetSuper();
    }
}
    

