package com.su.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/test3")
public class Test3_reqMapping {

    @RequestMapping("/t3")    // localhost:8080/test3/t3
    public String test3(Model model) {

        model.addAttribute("msg", "hello");

        return "test2";
    }
}
