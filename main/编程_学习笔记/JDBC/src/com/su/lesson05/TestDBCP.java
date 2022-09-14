package com.su.lesson05;

import com.su.lesson05.utils.JdbcUtils_DBCP;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class TestDBCP {
    public static void main(String[] args) {
        Connection conn = null;
        // prepareStatement: 可以防止sql注入
        PreparedStatement st = null;
        ResultSet rs = null;

        try {
            conn = JdbcUtils_DBCP.getConnection();

            // 区别
            // 使用 ? 占位符代替参数
            String sql = "INSERT INTO `user`(id,username,`password`)VALUES(?,?,?)";

            String sql2 = "DELETE FROM user WHERE id = ?";
            String sql3 = "UPDATE user SET username=? WHERE id = ?";

            // 预编译SQL,先写sql,然后不执行
            st = conn.prepareStatement(sql);

            // 手动给参数赋值
            // 给 values 里面的 ? 赋值\
            // parameterIndex: 第几个问号(从1开始)
            // x: 要附的值

            st.setInt(1, 29);
            st.setObject(2, "BBF");
            st.setObject(3, "pwd29");

            //执行
            int i = st.executeUpdate();
            if (i > 0) {
                System.out.println("插入成功");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils_DBCP.release(conn, st, rs);
        }
    }
}
