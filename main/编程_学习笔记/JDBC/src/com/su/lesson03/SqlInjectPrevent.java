package com.su.lesson03;

import com.su.lesson02.utils.JdbcUtils;


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SqlInjectPrevent {
    public static void main(String[] args) {

        login("AAA","pwd01");

        login("'or '1=1","'or '2=2");
    }

    // 登录业务
    public static void login(String username,String password){

        Connection conn = null;
        // prepareStatement: 可以防止sql注入
        PreparedStatement st = null;
        ResultSet rs = null;

        try {
            conn = JdbcUtils.getConnection();

            // 区别
            // 使用 ? 占位符代替参数
            // 如果传入了引号,会被直接 转义
            String sql = "SELECT * FROM user WHERE username = ? AND password = ?";

            // 预编译SQL,先写sql,然后不执行
            st = conn.prepareStatement(sql);

            st.setString(1, username);
            st.setString(2, password);

            //执行
            rs = st.executeQuery();

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
