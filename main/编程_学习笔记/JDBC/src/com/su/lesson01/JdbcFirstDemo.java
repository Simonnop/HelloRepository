package com.su.lesson01;

import java.sql.*;

// 我的第一个JDBC程序
public class JdbcFirstDemo {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 1.加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver"); // 固定写法,加载驱动,不同版本可能不一样

        // 2.用户信息与url\
        // jdbc:mysql://localhost:3306  mysql 默认 url
        // jdbctemplate 数据库名
        // useUnicode=true&characterEncoding=utf-8&useSSL=true  编码,安全连接设置
        String url = "jdbc:mysql://localhost:3306/jdbctemplate?useUnicode=true&characterEncoding=utf-8&useSSL=true";
        String username = "root";
        String password = "123456";

        // 3.连接成功,建立数据库对象
        Connection connection = DriverManager.getConnection(url,username,password);

        // 4.执行sql语句的对象
        Statement statement = connection.createStatement();

        // 5.执行sql的对象 去 执行sql,查看返回结果
        String sql = "SELECT * FROM user";

        ResultSet resultSet = statement.executeQuery(sql); // 查询操作,返回的结果集,封装了所有的结果
        // statement.executeUpdate(sql2); 更新,插入,删除 都使用 Update 方法,返回受影响的行数

        while (resultSet.next()){ // 如果有下一条
            System.out.println("id="+resultSet.getObject("id"));
            System.out.println("username="+resultSet.getObject("username"));
            System.out.println("password="+resultSet.getObject("password"));
            System.out.println("email="+resultSet.getObject("email"));
            System.out.println("gender="+resultSet.getObject("gender"));
            System.out.println("birth="+resultSet.getObject("birth"));
            System.out.println("====================================================");
        }

        /*
        resultSet.getObject(); // 不知道类型时使用
        resultSet.getInt();
        resultSet.getArray();
        resultSet.getDate();
        resultSet.getBigDecimal()

        resultSet.next();  (指针)移动到下一条
        resultSet.previous();  移动到上一条
        resultSet.beforeFirst();  移动到最前面
        */

        // 6.释放连接,必须完成
        resultSet.close();
        statement.close();
        connection.close();
    }
}
