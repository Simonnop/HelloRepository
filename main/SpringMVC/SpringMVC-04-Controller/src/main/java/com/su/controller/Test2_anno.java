package com.su.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class Test2_anno {

    @RequestMapping("test2")
    public String hello(Model model) {

        model.addAttribute("msg", "hello");

        return "test2";
    }
}
