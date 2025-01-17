package com.example.JdbcTemplate;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

@SpringBootTest
class JdbcTemplateApplicationTests {

	// DI注入数据源
	@Autowired
	DataSource dataSource;

	@Test
	void contextLoads() throws SQLException {

		//看一下默认数据源
		System.out.println(dataSource.getClass());
		//建立连接
		Connection connection = dataSource.getConnection();
		System.out.println(connection);
		//关闭连接
		connection.close();
	}

}
