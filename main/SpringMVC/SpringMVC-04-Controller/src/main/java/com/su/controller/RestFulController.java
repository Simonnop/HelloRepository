package com.su.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class RestFulController {

    // 原来的: localhost:8080/add1?a=1&b=2

    @RequestMapping("/add1")
    public String test1(int a, int b, Model model) {

        model.addAttribute("msg", a + b);

        return "test2";
    }

    // RestFul: localhost:8080/add2/1/2
    @RequestMapping("/add2/{a}/{b}")
    public String test2(@PathVariable int a, @PathVariable int b, Model model) {

        model.addAttribute("msg", a + b);

        return "test2";
    }

    // RestFul: localhost:8080/add3/1/2
    // 加入第二个参数: 仅限 某方法 请求
    // 不支持的方法无效,报 405
    // 可以写 @RequestMapping(value = "/add3/{a}/{b}",method = RequestMethod.DELETE)
    // 一般写
    @DeleteMapping("/add3/{a}/{b}")
    public String test3(@PathVariable int a, @PathVariable int b, Model model) {

        model.addAttribute("msg", a + b);

        return "test2";
    }

    // 此外还有
    /*
        @GetMapping
        @PostMapping
        @PutMapping
        @DeleteMapping
        @PatchMapping
    */

}
