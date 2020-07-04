#!/usr/bin/env python
# -*- coding: utf-8 -*-

from case import Case
from case_load import CaseLoad
import xlwt
import os


class HandleCase(object):
    ##处理Excel表信息的总入口

    def __init__(self, excel_path, config):
        ##暂时写死路径，后续通过配置文件传入
        # excel_path = "D:\\python_demo\\Hamster\\test\\test.xls"
        # log path从配置文件读取
        # case_path = cfg.get("path","log_path")
        print("excel Path {}".format(excel_path))
        index = excel_path.rfind("/")
        print("case path {}".format(os.path.abspath(excel_path[:index])))
        case_path = os.path.abspath(excel_path[:index])
        self.log_path_list = self._init_log_path_list(case_path)
        print(self.log_path_list)
        self.current_index = 0
        case_loader = CaseLoad(excel_path, config=config)
        self.case_list = case_loader.case_load()

        self.sheet_name = config.get("excel", "sheet_name")
        self.case_name = config.get("excel", "case_name")
        self.case_title = config.get("excel", "case_title")
        self.case_step = config.get("excel", "case_step")
        self.case_except = config.get("excel", "case_except")
        self.case_log = config.get("excel", "case_log")
        self.case_result = config.get("excel", "case_result")
        self.case_note = config.get("excel", "case_note")
        self.case_review = config.get("excel", "case_review")

    def _init_log_path_list(self, case_dir):
        ##初始化所有case path路径下的log文件
        log_path_list = list()
        for path, _, names in os.walk(case_dir):
            print(names)
            ##此处可做一个过滤器
            for name in names:
                if name.lower().endswith("log"):
                    log_path_list.append(os.path.join(path, name))
        return log_path_list

    def get_case_names(self):
        case_names = map(lambda x: x.get_case_name(), self.case_list)
        return list(case_names)

    def get_current_case(self):
        # print("---###--- current index:{}".format(self.current_index))
        return self.case_list[self.current_index]

    def get_current_case_name(self):
        return self.get_current_case().get_case_name()

    def get_current_case_title(self):
        return self.get_current_case().get_case_title()

    def set_current_case_title(self, case_title):
        self.get_current_case().set_case_title(case_title)

    def get_current_case_detail(self):
        return self.get_current_case().get_case_detail()

    def get_current_case_except(self):
        return self.get_current_case().get_case_except()

    def get_current_case_log(self):
        if self.get_current_case().get_case_log_path():
            log_path = self.get_current_case().get_case_log_path()
        else:
            log_path = self._locate_log_path()
        print("log path: {}".format(log_path))
        if log_path:
            ##待适配为读取文件内容
            log_list = []
            with open(log_path, "r", encoding="ISO-8859-1") as f:
                for log in f.readlines():
                    log_list.append(log)
            # log = log_path
            self.set_current_log(log_list)
        return self.get_current_case().get_case_log()

    def set_current_log(self, log):
        self.get_current_case().set_case_log(log)

    def set_current_log_path(self, log_path):
        self.get_current_case().set_case_log_path(log_path)

    def _locate_log_path(self):
        ##根据case name 定位 同名的log文件，不区分大小写
        case_name = self.get_current_case().get_case_name()
        for log in self.log_path_list:
            print("cp {} with {}".format(case_name, log))
            if not log.lower().split("\\")[-1].find(case_name.lower()) == -1:
                print("-----------------{}".format(log))
                return log
        return None

    def set_current_case_result(self, result):
        self.get_current_case().set_case_result(result)

    def get_current_case_result(self):
        return self.get_current_case().get_case_result()

    def set_current_case_note(self, note):
        self.get_current_case().set_case_note(note)

    def get_current_case_note(self):
        return self.get_current_case().get_case_note()

    def set_current_case_review(self, review):
        self.get_current_case().set_case_review(review)

    def get_current_case_review(self):
        return self.get_current_case().get_case_review()

    def export_case_to_excel(self, excel_path):
        ##将内存中数据输出指定Excel表
        new_case_list = list()
        # new_case_list.append([self.case_name,self.case_step,self.case_log,self.case_result])
        new_case_list.append(
            [
                self.case_name,
                self.case_title,
                self.case_step,
                self.case_except,
                self.case_result,
                self.case_note,
                self.case_review,
            ]
        )
        for case in self.case_list:
            new_case_list.append(
                [
                    case.get_case_name(),
                    case.get_case_title(),
                    case.get_case_detail(),
                    case.get_case_except(),
                    case.get_case_result(),
                    case.get_case_note(),
                    case.get_case_review(),
                ]
            )
        myWorkbook = xlwt.Workbook()
        mySheet = myWorkbook.add_sheet(self.sheet_name)
        for i in range(len(new_case_list)):
            for j in range(len(new_case_list[i])):
                mySheet.write(i, j, new_case_list[i][j])
        myWorkbook.save(excel_path)

    def next(self):
        ##下一个case
        self.current_index += 1

    def set_index(self, index):
        self.current_index = index

    def located_case(self, case_name):
        for index in range(len(self.case_list)):
            if self.case_list[index].get_case_name() == case_name:
                self.current_index = index
                break
        print("located failed")
