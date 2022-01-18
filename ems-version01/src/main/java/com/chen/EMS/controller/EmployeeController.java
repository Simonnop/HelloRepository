package com.chen.EMS.controller;

import com.chen.EMS.dao.DepartmentDao;
import com.chen.EMS.dao.EmployeeDao;
import com.chen.EMS.pojo.Department;
import com.chen.EMS.pojo.Employee;
import javafx.scene.input.DataFormat;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.propertyeditors.CustomDateEditor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.*;

import javax.jws.WebResult;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Collection;
import java.util.Date;

@Controller
public class EmployeeController {

    @Autowired
    EmployeeDao employeeDao;
    @Autowired
    DepartmentDao departmentDao;

    @RequestMapping("/emps")
    public String list(Model model){
        Collection<Employee> employees = employeeDao.getAll();
        model.addAttribute("emps",employees);
        return "emp/list";
    }

    @GetMapping("/addEmployee")
    public String toAddpage(Model model){
        //查出所有部门的信息
        Collection<Department> departments = departmentDao.getDepartments();
        model.addAttribute("departments",departments);
        return "emp/addEmployee";
    }

    @PostMapping("/addEmployee")
    public String AddEmployee(Employee employee){
        employeeDao.save(employee);//调用底层业务方法保存员工信息
        return "redirect:/emps";
    }

    //去员工的修改页面
    @GetMapping("/emp/{id}")
    public String toUpdateEmp(@PathVariable("id")Integer id,Model model){
        //查出原来的数据
        Employee employee = employeeDao.getEmployById(id);

        model.addAttribute("emp", employee);
        //查出所有部门的信息
        Collection<Department> departments = departmentDao.getDepartments();
        model.addAttribute("departments",departments);
        return "emp/update";
    }

    //删除员工
    @GetMapping("/deleteEmp/{id}")
    public String deleteEmp(@PathVariable("id")Integer id){
        //查出原来的数据
        employeeDao.deleteEmployById(id);
        return "redirect:/emps";
    }


}
