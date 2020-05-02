#!/usr/bin/env python
# -*- coding: utf-8 -*-

from case import Case
from case_load import CaseLoad
import xlwt

class HandleCase(object):

    def __init__(self,excel_path):
        excel_path = "D:\\python_demo\\Hamster\\test\\test.xls"
        self.current_index = 0
        case_loader = CaseLoad(excel_path)
        self.case_list = case_loader.case_load()
        self.case_name = "Case_name"
        self.case_step = "Case_step"
        self.case_log = "Log"
        self.case_result = "Result"

    def get_current_case(self):
        return  self.case_list[self.current_index]

    def get_current_case_name(self):
        return self.get_current_case().get_case_name()

    def get_current_case_detail(self):
        return self.get_current_case().get_case_detail()

    def get_current_case_log(self):
        return self.get_current_case().get_case_log()

    def set_current_log(self,log):
        self.get_current_case().set_case_log(log)

    def set_current_case_result(self,result):
        self.get_current_case().set_case_result(result)

    def export_case_to_excel(self,excel_path):
        new_case_list = list()
        new_case_list.append([self.case_name,self.case_step,self.case_log,self.case_result])
        for case in self.case_list:
            new_case_list.append([case.get_case_name(),case.get_case_detail(),
                                 case.get_case_log_path(),case.get_case_result()])
        myWorkbook = xlwt.Workbook()
        mySheet = myWorkbook.add_sheet('text_excel')
        for i in range(len(new_case_list)):
            for j in range(len(new_case_list[i])):
                mySheet.write(i,j,new_case_list[i][j])
        myWorkbook.save(excel_path)

    def next(self):
        self.current_index += 1


    #pass

if __name__ == '__main__':
    export_path="D:\\python_demo\\Hamster\\test\\test1.xls"
    ha = HandleCase("")
    print("0:{}".format(ha.get_current_case()))
    ha.set_current_case_result("True")
    ha.set_current_log("log")
    print("0.1:{}".format(ha.get_current_case()))
    ha.next()
    print("1:{}".format(ha.get_current_case()))
    ha.set_current_case_result("False")
    ha.set_current_log("log2")
    ha.next()
    ha.export_case_to_excel(export_path)
