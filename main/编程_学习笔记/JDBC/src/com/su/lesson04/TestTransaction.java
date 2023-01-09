package com.su.lesson04;

import com.su.lesson02.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class TestTransaction {
    public static void main(String[] args) {

        Connection conn = null;
        // prepareStatement: 可以防止sql注入
        PreparedStatement st = null;
        ResultSet rs = null;

        try {
            conn = JdbcUtils.getConnection();

            // 关闭数据库自动提交,自动开启事务
            conn.setAutoCommit(false);  // 开启事务

            String sql = "SELECT * FROM user";

            st = conn.prepareStatement(sql);
            // 执行
            st.executeQuery();
            // 提交事务
            conn.commit();
            System.out.println("执行成功");

        } catch (SQLException e) {
/*            try {
                conn.rollback(); // 如果失败就回滚
            } catch (SQLException ex) {
                ex.printStackTrace();
            }*/
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, st, rs);
        }
    }
}
