package com.example.JdbcTemplate.Controller;

import com.example.JdbcTemplate.Dao.UserDao;
import com.example.JdbcTemplate.Model.User;
import com.example.JdbcTemplate.utils.PageList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.text.ParseException;
import java.util.List;

@Controller
public class UserController {

    @Autowired
    UserDao userDao;

    @GetMapping
    public String showList(Model model) throws ParseException {
        List<User> users = userDao.getUserList();
        model.addAttribute("users", users);

        return "userlist";
    }

    @GetMapping("/user/{pageSize}/{currentPage}")
    public PageList<User> UserPageList(@PathVariable("pageSize") int pageSize, @PathVariable("currentPage") int currentPage) throws ParseException {
        return userDao.getUserListByPage(currentPage,pageSize);
    }

    @GetMapping({"/user/listByPage/{currentPage}","localhost:8080/user/listByPage/{currentPage}"})
    public String showListByPage(@PathVariable("currentPage") int currentPage,Model model) throws ParseException {
        PageList<User> userPageList = UserPageList(7, currentPage);

        //起不同的名，与showList区分一下
        List<User> usersByPage = userPageList.getDataList();
        model.addAttribute("usersByPage",usersByPage);

        //获取总的页数
        int pageNumber = userPageList.getPageNumber();
        model.addAttribute("pageNumber",pageNumber);

        return "userlist";
    }

}
