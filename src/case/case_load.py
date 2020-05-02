#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd,xlwt
from case import Case

class CaseLoad(object):

    def __init__(self,in_case_path):
        self.input_case_path = in_case_path
        self.sheet_name = "Sheet1"
        self.case_name = "Case_name"
        self.case_step = "Case_step"
        self.case_except = "Case_except"
        self.case_other = "other"
        '''
        self.case_log = "Log"
        self.case_result = "Result"
        '''

    def _init_excel(self):
        data = xlrd.open_workbook(self.input_case_path)
        self.table = data.sheet_by_name(self.sheet_name)
        self.nrows = self.table.nrows
        print("nrows :" + str(self.nrows))
        self.ncols = self.table.ncols
        print("ncows :" + str(self.ncols))
        self.case_name_index = self.__get_col_by_name(self.case_name)
        self.case_step_index = self.__get_col_by_name(self.case_step)
        self.case_except_index = self.__get_col_by_name(self.case_except)
        self.case_other_index = self.__get_col_by_name(self.case_other)

    def case_load(self):
        self._init_excel()
        case_list = list()
        for i in range(1,self.nrows):
            case_name = self.table.cell(i,self.case_name_index).value
            case_step = self.table.cell(i,self.case_step_index).value
            print("ADD : "+case_name + case_step)
            case_list.append(Case(case_name,case_step))
        return case_list

    def __get_col_by_name(self,name):
        name_col = 0
        for col in range(self.ncols):
            if self.table.cell(0,col).value == name:
                name_col = col
                break
        return name_col
    '''
    def export_excel(self,output_case_path,case_list):
        new_case_list = list()
        new_case_list.append([self.case_name,self.case_step,self.case_log,self.case_result])
        for case in case_list:
            new_case_list.append([case.get_case_name(),case.get_case_detail(),
                                 case.get_case_log_path(),case.get_case_result()])
        myWorkbook = xlwt.Workbook()
        mySheet = myWorkbook.add_sheet('text_excel')
        for i in range(len(new_case_list)):
            for j in range(len(new_case_list[i])):
                mySheet.write(i,j,new_case_list[i][j])
        myWorkbook.save(output_case_path)
    #pass

if __name__ == '__main__':
    cl = CaseLoad("D:\\python_demo\\Hamster\\test\\test.xls")
    re = cl.case_load()
    #print(re)
    cl.export_excel("D:\\python_demo\\Hamster\\test\\test1.xls",re)
    '''