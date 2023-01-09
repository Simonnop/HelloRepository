package com.su.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController  // 在类上直接使用 @RestController ，这样子，里面所有的方法都只会返回 json 字符串
public class Test5_json {
    @RequestMapping(value = "/json")
    public String json1() {
        //创建一个jackson的对象映射器，用来解析数据
        // ObjectMapper mapper = new ObjectMapper();
        //创建一个对象
        // User user = new User("秦疆1号", 3, "男");
        //将我们的对象解析成为json格式
        // String str = mapper.writeValueAsString(user);
        //由于@ResponseBody注解，这里会将str转成json格式返回；十分方便

        // 以上不用看,就是生成 json

        String str = "test";
        str += ",hello";
        return str;
        // 直接返回字符串
    }
}
