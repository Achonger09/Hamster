#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Case(object):
    """
    Case 类，存放Case信息的字段
    """

    def __init__(self, case_name, case_title=None, case_detail=None, case_except=None):
        self.case_name = case_name
        self.case_detail = case_detail
        self.case_except = case_except
        self.case_title = case_title
        self.case_log_path = None
        self.case_log = None
        self.case_result = None
        self.case_note = None
        self.case_review = None

    def get_case_title(self):
        return self.case_title

    def set_case_title(self, case_title):
        self.case_title = case_title

    def get_case_except(self):
        return self.case_except

    def set_case_note(self, note):
        self.case_note = note

    def get_case_note(self):
        return self.case_note

    def set_case_review(self, review):
        self.case_review = review

    def get_case_review(self):
        return self.case_review

    def get_case_name(self):
        return self.case_name

    def get_case_detail(self):
        return self.case_detail

    def set_case_log_path(self, case_log_path):
        self.case_log_path = case_log_path

    def get_case_log_path(self):
        return self.case_log_path

    def set_case_result(self, case_result):
        print("----------case : set result:{}".format(case_result))
        self.case_result = case_result

    def get_case_result(self):
        print("------------case : get result :{}".format(self.case_result))
        return self.case_result

    def get_case_log(self):
        return self.case_log

    def set_case_log(self, log):
        self.case_log = log
