package com.su.lesson02;

import com.su.lesson02.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestInsert {
    public static void main(String[] args) throws SQLException {

        Connection conn = null;
        Statement st = null;
        ResultSet rs = null;

        String sql = "INSERT INTO `user`(id,username,`password`)VALUES(28,'AZZ','pwd27')";

        try {
            conn = JdbcUtils.getConnection(); //获取数据库连接
            st = conn.createStatement();
            //更新,插入,删除 都使用 Update
            int i = st.executeUpdate(sql);
            if (i > 0) {
                System.out.println("插入成功!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, st, rs);
        }
    }
}
