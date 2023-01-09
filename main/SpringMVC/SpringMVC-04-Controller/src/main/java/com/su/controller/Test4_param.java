package com.su.controller;

import com.su.pojo.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Controller
@RequestMapping("/param")
public class Test4_param {

    // 方法的参数有很多种类型

    // model
    @RequestMapping("/t3")    // localhost:8080/test3/t3
    public String test3(Model model) {

        model.addAttribute("msg", "hello");

        return "test2";
    }

    // 获取参数
    @RequestMapping("/add2/{a}/{b}")
    public String test2(@PathVariable int a, @PathVariable int b, Model model) {

        model.addAttribute("msg", a + b);

        return "test2";
    }

    // 获取 req resp
    @RequestMapping("/result/t1")
    public void test1(HttpServletRequest req, HttpServletResponse rsp) throws IOException {
        rsp.getWriter().println("Hello,Spring BY servlet API");
    }

    // 获取实体类
    // 根据参数构造对象
    // http://localhost:8080/param/user?name=kuangshen&id=1&age=15
    @RequestMapping("/user")
    public String user(User user){
        System.out.println(user);
        return "test2";
    }

    // 提交的域名称和处理方法的参数名不一致
    // 如提交 username 方法参数是 name
    // 提交数据 : http://localhost:8080/param/hello?username=Simonnop

    //@RequestParam("username") : username提交的域的名称 .
    @RequestMapping("/hello")
    public String hello(@RequestParam("username") String name){
        System.out.println(name);
        return "hello";
    }
}
