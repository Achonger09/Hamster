#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd, xlwt
from case import Case


class CaseLoad(object):
    ##初始化Excel表信息，将其加载到caselist中

    def __init__(self, in_case_path, config):
        self.input_case_path = in_case_path
        ##以下信息带适配为从配置文件获取

        self.sheet_name = config.get("excel", "sheet_name")
        self.case_name = config.get("excel", "case_name")
        self.case_title = config.get("excel", "case_title")
        self.case_step = config.get("excel", "case_step")
        self.case_except = config.get("excel", "case_except")
        self.case_log = config.get("excel", "case_log")
        self.case_result = config.get("excel", "case_result")
        self.case_note = config.get("excel", "case_note")
        self.case_review = config.get("excel", "case_review")

    def _init_excel(self):
        data = xlrd.open_workbook(self.input_case_path)
        self.table = data.sheet_by_name(self.sheet_name)
        self.nrows = self.table.nrows
        print("nrows :" + str(self.nrows))
        self.ncols = self.table.ncols
        print("ncows :" + str(self.ncols))
        self.case_name_index = self.__get_col_by_name(self.case_name)
        self.case_title_index = self.__get_col_by_name(self.case_title)
        self.case_step_index = self.__get_col_by_name(self.case_step)
        self.case_except_index = self.__get_col_by_name(self.case_except)
        self.case_result_index = self.__get_col_by_name(self.case_result)
        self.case_note_index = self.__get_col_by_name(self.case_note)
        self.case_review_index = self.__get_col_by_name(self.case_review)
        # self.case_other_index = self.__get_col_by_name(self.case_other)

    def case_load(self):
        self._init_excel()
        case_list = list()
        for i in range(1, self.nrows):
            case_name = self.table.cell(i, self.case_name_index).value
            case_title = self.table.cell(i, self.case_title_index).value
            case_step = self.table.cell(i, self.case_step_index).value
            case_except = self.table.cell(i, self.case_except_index).value
            case_result = self.table.cell(i, self.case_result_index).value
            case_note = self.table.cell(i, self.case_note_index).value
            case_review = self.table.cell(i, self.case_review_index).value

            if case_name.replace(" ", "") == "":
                continue
            print("ADD : " + case_name + case_step + case_except)
            ##目前只使用casename,casestep初始化，后续有变动在适配
            case_list.append(
                Case(
                    case_name,
                    case_title,
                    case_step,
                    case_except,
                    case_result=case_result,
                    case_note=case_note,
                    case_review=case_review,
                )
            )
        return case_list

    def __get_col_by_name(self, name):
        name_col = 0
        for col in range(self.ncols):
            if self.table.cell(0, col).value == name:
                name_col = col
                break
        return name_col
