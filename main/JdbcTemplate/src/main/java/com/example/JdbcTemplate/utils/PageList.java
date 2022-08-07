package com.example.JdbcTemplate.utils;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.ArrayList;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class PageList<T> {

    private int pageSize;   //单页最大数据量

    private int dataNumber; //Java类T 总的数据量

    private int pageNumber; //总的页数 总的页数=(总的数据量%单页最大数据量)==0?(总的数据量/单页最大数据量):((总的数据量/单页最大数据量)+1)

    private int currentPage; //当前页

    private List<T> dataList = new ArrayList<T>(); //当前页的全部数据

    public PageList(int currentPage,int pageSize,int dataNumber){
        this.currentPage = currentPage;
        this.pageSize = pageSize;
        pageNumber = (dataNumber%pageSize==0?(dataNumber/pageSize):(dataNumber/pageSize+1));
    }

}
