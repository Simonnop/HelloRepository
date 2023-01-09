package com.su.lesson02;

import com.su.lesson02.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestSelect {
    public static void main(String[] args) {

        Connection conn = null;
        Statement st = null;
        ResultSet rs = null;

        String sql = "SELECT * FROM user";

        try {
            conn = JdbcUtils.getConnection();
            st = conn.createStatement();
            // 查询使用 executeQuery()
            rs = st.executeQuery(sql);

            while(rs.next()){
                System.out.println(rs.getObject("username"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, st, rs);
        }
    }
}
