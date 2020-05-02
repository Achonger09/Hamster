#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Case(object):
    '''
    Case 类
    '''
    def __init__(self,case_name,case_detail):
        self.case_name =case_name
        self.case_detail = case_detail
        self.case_log_path = None
        self.case_log = None
        self.case_result = None

    def get_case_name(self):
        return self.case_name

    def get_case_detail(self):
        return self.case_detail

    def set_case_log_path(self,case_log_path):
        self.case_log_path = case_log_path

    def get_case_log_path(self):
        return self.case_log_path

    def set_case_result(self,case_result):
        self.case_result = case_result

    def get_case_result(self):
        return self.case_result

    def get_case_log(self):
        return self.case_log

    def set_case_log(self,log):
        self.case_log = log
