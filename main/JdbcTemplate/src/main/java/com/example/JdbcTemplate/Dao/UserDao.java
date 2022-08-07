package com.example.JdbcTemplate.Dao;

import com.example.JdbcTemplate.Model.User;
import com.example.JdbcTemplate.utils.PageList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;

@Repository
public class UserDao {

    @Autowired
    JdbcTemplate jdbcTemplate;

    //获取所有的user信息
    public List<User> getUserList() throws ParseException {
        //连接数据库

        // 定义执行的sql语句
        String sql = "select * from `user`";

        // 调用JdbcTemplate对象,执行sql语句,并接收
        /*
        *   List -> [{id1,pwd1},{id2,pwd2}]
        *
        *   Map 是键值对
        *   id:1
        *   username:AAA
        *   ...
        *
        * */

        //调用对象,使用方法执行sql
        List<Map<String,Object>> userList = jdbcTemplate.queryForList(sql);


        //同时定义一个List来接收sql执行结果(Object类 -> User类)
        ArrayList<User> users = new ArrayList<User>();
        // 对列表中26行数据依次进行转化,转为User对象
        for (int i = 0; i<userList.size(); i++){
            // Number是整数和浮点数共有的一个父类
            int id = ((Number)userList.get(i).get("id")).intValue();
            String username = (String) userList.get(i).get("username");
            String password = (String) userList.get(i).get("password");
            String email = (String) userList.get(i).get("email");
            int gender = ((Number) userList.get(i).get("gender")).intValue();

            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
            System.out.println(userList.get(i).get("birth").getClass());
            Date birth = dateFormat.parse((String) userList.get(i).get("birth"));

            User user = new User(id, username, password, email, gender, birth);
            users.add(user);
        }

        return users;
    }

    //分页功能实现，获取分页数据
    //前端页面点击分页器时调用此函数
    public PageList<User> getUserListByPage(int currentPage, int pageSize) throws ParseException {
        //获取总数据量
        List<User> userList = getUserList();
        int dataNumber = userList.size();


        //设置当前页面和每个页面的最大数据量
        //这里我设置每个页面的最大数据量为7
        PageList<User> userPageList = new PageList<>(currentPage, pageSize,dataNumber);

        //获取所有的user数据，易知总的数据量为26
        userPageList.setDataNumber(jdbcTemplate.queryForObject("SELECT count(id) FROM `user`",Integer.class));

        //根据当前页的情况来确定当前页的展示数据列表
        if (userPageList.getCurrentPage()==userPageList.getPageNumber()){
            //当前页为总页面的最后一页
            userPageList.setDataList(jdbcTemplate.query("SELECT * FROM `user` limit ?,?",new BeanPropertyRowMapper<>(User.class),
                    (currentPage-1)*pageSize,userPageList.getDataNumber()-(currentPage-1)*pageSize));
        }else {
            userPageList.setDataList(jdbcTemplate.query("SELECT * FROM `user` limit ?,?",new BeanPropertyRowMapper<>(User.class),
                    (currentPage-1)*pageSize,pageSize));
        }
        return userPageList;
    }

}
