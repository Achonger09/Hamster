#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os


class ConfigLoad(object):
    """
    读取config.ini文件内容，并返回
    """

    def __init__(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        # print(root_path)
        ##目前路径固定，暂不修改
        config_path = os.path.join(root_path, "C:\\.hamster_config\\config.ini")
        # print(config_path)
        conf = configparser.ConfigParser()
        if os.path.exists(config_path):
            conf.read(config_path, encoding="UTF-8")
        else:
            ## 无配置文件,则使用此配置
            conf["excel"] = {
                "sheet_name": "测试用例集",
                "case_name": "用例编号",
                "case_title": "用例标题",
                "case_step": "测试步骤",
                "case_except": "预期结果",
                "case_log": "Log",
                "case_result": "检视结果",
                "case_note": "备注",
                "case_review": "检视人",
            }
        self.conf = conf

    def get(self, *args):
        return self.conf.get(*args)

    def options(self, session):
        return self.conf.items(session)


# if __name__ == "__main__":
#    config = ConfigLoad()
#    print(config.get("windows","root_title"))
