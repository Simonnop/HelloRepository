package com.su.lesson02;

import com.su.lesson02.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class SqlInject {
    public static void main(String[] args) {
        // 密码错误,不会执行
        login("AAA","pwd02");

        // sql注入: 利用sql漏洞获取数据
        // 查询语句中写入额外的条件语句,sql会被拼接
        login("'or '1=1","'or '2=2");
    }

    // 登录业务
    public static void login(String username,String password){

        Connection conn = null;
        Statement st = null;
        ResultSet rs = null;

        String sql = "SELECT * FROM user WHERE username = '"+username+"'AND password = '"+password+"'";

        try {
            conn = JdbcUtils.getConnection();
            st = conn.createStatement();
            // 查询使用 executeQuery()
            rs = st.executeQuery(sql);

            while(rs.next()){
                System.out.println(rs.getObject("birth"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, st, rs);
        }

    }
}
