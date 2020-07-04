#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import sys, os
from handle_case import HandleCase
from config_load import ConfigLoad
from tkinter import filedialog
from tkinter.simpledialog import askstring
import re


class HandleWindows(object):
    ##处理windows窗体函数，目前纸打印窗体，具体功能待添加
    ##窗口信息计划从配置文件读取，目前都是写死的
    def __init__(self, config):
        self.pwd = os.getcwd()
        print(self.pwd)
        root_size = "1170x600"
        # root_size = cfg.get("windows","root_size")
        # root_title = cfg.get("windows","root_title")
        # log_path=cfg.get("path","log_path")
        root_title = "windows"
        log_path = ""
        print(log_path)
        self.log_path = log_path
        # excel_path = cfg.get("path","excel_path")
        excel_path = ""
        root_windows = tk.Tk()
        root_windows.title(root_title)
        root_windows.geometry(root_size)
        if excel_path and os.path.exists(excel_path) and os.path.isfile(excel_path):
            ha = HandleCase(excel_path, config=config)
        else:
            ha = None
        self.handle_case = ha
        self.root_windows = root_windows
        self.config = config
        # self.cfg = cfg

    def _show_case_list(
        self, text="Case List", f_width=220, f_height=520, b_width=28, b_height=27
    ):
        py_frame1 = tk.LabelFrame(
            self.root_windows, text="Case List", width=f_width, height=f_height
        )
        py_frame1.place(x=10, y=5)
        scroll = tk.Scrollbar()
        sb = tk.Scrollbar(py_frame1)
        theLB = tk.Listbox(
            py_frame1,
            selectmode=tk.SINGLE,
            width=b_width,
            height=b_height,
            yscrollcommand=sb.set,
        )
        # theLB.insert(tk.INSERT, text)

        # theLB.place(x=5, y=5)
        if self.handle_case:
            for case_name in self.handle_case.get_case_names():
                theLB.insert(tk.END, case_name)
        self.theLB = theLB
        theLB.pack(side=tk.LEFT, fill=tk.BOTH)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        sb.config(command=theLB.yview)
        # 双击事件
        theLB.bind("<Double-Button-1>", self._reflush_case)
        theLB.bind("<Control-n>", self._open_excel)
        # for i in range(30):
        #    theLB.insert(tk.END,"Test_abcdefghjgl_00"+str(i))

    def _show_case_title(
        self, text="Title", f_width=333, f_height=50, b_width=45, b_height=1
    ):
        py_frame2 = tk.LabelFrame(
            self.root_windows, text="Title", width=f_width, height=f_height
        )
        py_frame2.place(x=240, y=5)
        if self.handle_case:
            text = self.handle_case.get_current_case_title()
        else:
            text = ""
        theLabel = tk.Label(
            py_frame2,
            width=b_width,
            height=b_height,
            text=text,
            wraplength=300,
            justify="left",
            anchor="nw",
        )
        theLabel.place(x=5, y=5)

    def _show_case_steps(
        self, text="Steps", f_width=340, f_height=235, b_width=45, b_height=16
    ):
        py_frame2 = tk.LabelFrame(
            self.root_windows, text="Steps", width=f_width, height=f_height
        )
        py_frame2.place(x=240, y=55)
        if self.handle_case:
            text = self.handle_case.get_current_case_detail()
        else:
            text = ""
        sb = tk.Scrollbar(py_frame2)
        theLabel = tk.Text(
            py_frame2, width=b_width - 1, height=b_height, yscrollcommand=sb.set
        )
        theLabel.insert(tk.INSERT, text)
        theLabel.pack(side=tk.LEFT, fill=tk.BOTH)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        sb.config(command=theLabel.yview)

    def _show_case_except(
        self, text="Except", f_width=340, f_height=235, b_width=45, b_height=16
    ):
        py_frame2 = tk.LabelFrame(
            self.root_windows, text="Excepts", width=f_width, height=f_height
        )
        py_frame2.place(x=240, y=290)
        if self.handle_case:
            text = self.handle_case.get_current_case_except()
        else:
            text = ""
        # text = ""
        scroll = tk.Scrollbar()
        sb = tk.Scrollbar(py_frame2)
        print("---------------{}".format(text))
        # sb = tk.Scrollbar(py_frame2)
        theLabel = tk.Text(
            py_frame2, width=b_width - 1, height=b_height, yscrollcommand=sb.set
        )
        # theLabel.pack(side = tk.LEFT,fill = tk.BOTH)
        theLabel.insert(tk.INSERT, text)
        theLabel.pack(side=tk.LEFT, fill=tk.BOTH)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        sb.config(command=theLabel.yview)
        # sb.pack(side=tk.RIGHT, fill=tk.Y)
        # sb.config(command=theLabel.yview)
        # theLabel.place(x=5, y=5)

    def _show_case_logs(
        self, text="Logs", f_width=340, f_height=520, b_width=45, b_height=38
    ):
        py_frame3 = tk.LabelFrame(
            self.root_windows, text="Logs", width=f_width, height=f_height
        )
        py_frame3.place(x=590, y=5)
        if self.handle_case:
            context = self.handle_case.get_current_case_log()
        else:
            context = "None!!!"
        if not context:
            context = " "
        scroll = tk.Scrollbar()
        sb = tk.Scrollbar(py_frame3)
        # sb.place(x=316,y=5)
        # sb.pack(side=tk.RIGHT, fill=tk.Y)
        log_text = tk.Text(
            py_frame3, width=b_width - 1, height=b_height, yscrollcommand=sb.set
        )

        print("context:{}".format(context))
        # sb.config(command=log_text.yview)
        log_text.insert(tk.INSERT, context)
        # log_text.place(x=5, y=5)
        log_text.pack(side=tk.LEFT, fill=tk.BOTH)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        sb.config(command=log_text.yview)
        log_text.bind("<Control-f>", self._search_log)
        self.log_text = log_text

        sb.config(command=log_text.yview)

    def _show_case_result(
        self, text="Result", f_width=220, f_height=220, b_width=28, b_height=14
    ):
        py_frame4 = tk.LabelFrame(
            self.root_windows, text="Result", width=f_width, height=f_height
        )
        py_frame4.place(x=940, y=5)
        result_text = tk.Text(py_frame4, width=b_width, height=b_height)
        result_text.place(x=5, y=5)
        self.result_text = result_text
        if self.handle_case:
            result = self.handle_case.get_current_case_result()
        else:
            result = " "
        if not result:
            result = " "
        print("show windows result :{}".format(result))
        result_text.insert(tk.CURRENT, result)

    def _show_case_notes(
        self, text="Notes", f_width=220, f_height=220, b_width=28, b_height=14
    ):
        py_frame4 = tk.LabelFrame(
            self.root_windows, text="Notes", width=f_width, height=f_height
        )
        py_frame4.place(x=940, y=230)
        note_text = tk.Text(py_frame4, width=b_width, height=b_height)
        note_text.place(x=5, y=5)
        self.note_text = note_text
        # note_text.delete(0, 'end')
        if self.handle_case:
            note = self.handle_case.get_current_case_note()
        else:
            note = " "
        if not note:
            note = " "
        note_text.insert(tk.INSERT, note)

    def _show_case_reviewer(
        self, text="Reviewer", f_width=220, f_height=60, b_width=28, b_height=2
    ):
        py_frame4 = tk.LabelFrame(
            self.root_windows, text="Reviewer", width=f_width, height=f_height
        )
        py_frame4.place(x=940, y=462)
        review_text = tk.Text(py_frame4, width=b_width, height=b_height)
        review_text.place(x=5, y=5)
        self.review_text = review_text
        # review_text.delete(0, 'end')
        if self.handle_case:
            review = self.handle_case.get_current_case_review()
        else:
            review = " "
        if not review:
            review = " "
        review_text.insert(tk.INSERT, review)

    def _show_record_button(self):
        update_button1 = tk.Button(
            self.root_windows,
            bg="whitesmoke",
            text="Record Result",
            width=15,
            height=2,
            command=self._record_result,
        )
        update_button1.place(x=1000, y=535)

    def _show_import_button(self):
        update_button2 = tk.Button(
            self.root_windows,
            bg="whitesmoke",
            text="Import Logs",
            width=15,
            height=2,
            command=self._import_log,
        )
        update_button2.place(x=710, y=535)

    def _show_export_button(self):
        update_button3 = tk.Button(
            self.root_windows,
            bg="whitesmoke",
            text="Export Excel",
            width=15,
            height=2,
            command=self._save_excel,
        )
        update_button3.place(x=360, y=535)

    def _show_reflush_button(self):
        ##已废弃
        update_button3 = tk.Button(
            self.root_windows,
            bg="whitesmoke",
            text="import Case",
            width=15,
            height=2,
            command=self._open_excel,
        )
        update_button3.place(x=60, y=535)

    def _reflush_case(self, event):
        ##根据选择的caseName 刷新step，log
        case_index = self.theLB.curselection()
        print(case_index)
        if case_index[0]:
            print(case_index)
            self.handle_case.set_index(case_index[0])
            print(
                "context result :{},note:{}".format(
                    self.handle_case.get_current_case_result(),
                    self.handle_case.get_current_case_note(),
                )
            )
            ##没必要完全重画，待优化
            self._show_case_steps()
            self._show_case_logs()
            self._show_case_list()
            self._show_case_result()
            self._show_case_title()
            self._show_case_except()
            self._show_case_notes()
            self._show_case_reviewer()
            # self.result_text.delete("0.0", "end")

    def _record_result(self):
        ##记录用户数输入的result
        result_context = self.result_text.get("0.0", "end")
        print("record result:{}".format(result_context))
        self.handle_case.set_current_case_result(result_context)
        print(
            "after record result:{}".format(self.handle_case.get_current_case_result())
        )
        note_context = self.note_text.get("0.0", "end")
        print("record note:{}".format(note_context))
        self.handle_case.set_current_case_note(note_context)
        review_context = self.review_text.get("0.0", "end")
        print("record review:{}".format(review_context))
        self.handle_case.set_current_case_review(review_context)
        # self.result_text.delete("0.0","end")

    def _import_log(self):
        ##通过文件管理器导入log文件,指定初始目录
        log_path = filedialog.askopenfilename(initialdir=self.log_path)
        print(log_path)
        self.handle_case.set_current_log_path(log_path)
        self._show_case_logs()

    def _open_excel(self, event=None):
        ##通过文件管理器获取excel表路径
        case_path = filedialog.askopenfilename(initialdir=self.log_path)
        print(case_path)
        self.handle_case = HandleCase(case_path, self.config)
        self._show_case_list()
        self._show_case_title()
        self._show_case_except()
        self._show_case_steps()
        self._show_case_logs()
        self._show_case_result()
        self._show_case_notes()
        self._show_case_reviewer()

    def _save_excel(self):
        ##目前写死路径，后面改为时间戳形式的路径
        ##或者用户选择保存在哪里
        export_path = filedialog.asksaveasfilename(defaultextension=".xls")
        print(export_path)
        self.handle_case.export_case_to_excel(export_path)

    def _search_log(self, event):
        ## Ctrl + F触发
        print("ctl+f --->search")
        res = askstring("Search", "Key Words")
        print(res)
        context = self.handle_case.get_current_case_log()
        tmp_list = context.split(res)
        self.log_text.delete("0.0", "end")
        self.log_text.tag_delete("1.0", "end")
        self.log_text.tag_config("blue", foreground="blue")
        for index in range(len(tmp_list) - 1):
            self.log_text.insert(tk.CURRENT, tmp_list[index])
            self.log_text.insert(tk.CURRENT, res, "blue")
        self.log_text.insert(tk.CURRENT, tmp_list[-1])
        # self.log_text.place(x=5, y=5)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH)

    """
    ##废弃
    def _search_log(self,event):
        ##Ctrl+F触发此接口
        print("ctrl+f---->search")
        res = askstring("Search", "Key Words")
        print(res)
        context = self.handle_case.get_current_case_log()
        tmp_list= list()
        index_list = self._find_index_all(res,context,tmp_list)
        if not index_list[-1] == len(context):
            index_list.append(len(context))
        print(index_list)
        if not len(index_list) == 0:
            self.log_text.delete("0.0","end")
            self.log_text.tag_delete("1.0","end")
            self.log_text.tag_config('blue',foreground = 'blue')
            begin = 0
            for index in index_list:
                #self.log_text.tag_add('blue',index,index+len(res))
                print(begin,index+len(res))
                self.log_text.insert(tk.CURRENT,context[begin:index])
                self.log_text.insert(tk.CURRENT,context[index:index+len(res)],'blue')
                begin = index+len(res)
            self.log_text.place(x=5,y=5)

    def _find_index_all(self,key_word,context,index_list):
        ##搜寻所有关键字的下表，作为列表元素返回
        print("find {} in {}".format(key_word.lower(),context.lower()))
        if context == None or len(context) < len(key_word):
            return index_list
        end = context.lower().find(key_word.lower())
        if not end == -1:
            new_context = context[end+len(key_word):]
            if not len(index_list) == 0:
                end = end+len(key_word) + index_list[-1]
            index_list.append(end)
            return self._find_index_all(key_word,new_context,index_list)
        else:
            return index_list
    """

    def run_windows(self):
        self._show_case_list()
        self._show_case_title()
        self._show_case_steps()
        self._show_case_except()
        self._show_case_logs()
        self._show_case_result()
        self._show_case_notes()
        self._show_case_reviewer()
        self._show_export_button()
        self._show_import_button()
        self._show_reflush_button()
        self._show_record_button()
        tk.mainloop()


if __name__ == "__main__":
    config = ConfigLoad()
    # print(config.get("windows","root_title"))
    # windows = HandleWindows(config)
    windows = HandleWindows(config=config)
    windows.run_windows()
