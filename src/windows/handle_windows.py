#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import sys,os
sys.path.append(os.path.abspath('../config/'))
print(os.path.abspath('../config/'))
from config_load import ConfigLoad
from src.case.handle_case import  HandleCase
from tkinter import filedialog
from tkinter.simpledialog import askstring
import re

class HandleWindows(object):
    ##处理windows窗体函数，目前纸打印窗体，具体功能待添加
    ##窗口信息计划从配置文件读取，目前都是写死的
    def __init__(self,cfg):
        size = cfg.get("windows","size")
        root_windows = tk.Tk()
        root_windows.title("")
        root_windows.geometry("1170x600")
        export_path="D:\\python_demo\\Hamster\\test\\test2.xls"
        ha = HandleCase("D:\\python_demo\\Hamster\\test\\test.xls")
        self.handle_case = ha
        self.root_windows = root_windows

    def _show_case_list(self,text = "Case List",width = 220,height = 520):
        py_frame1 = tk.LabelFrame(self.root_windows,text = "Case List",width = 220,height = 520)
        py_frame1.place(x=10,y=5)
        theLB = tk.Listbox(py_frame1, selectmode=tk.SINGLE,width = 28, height=27)
        theLB.place(x=5,y=5)
        for case_name in self.handle_case.get_case_names():
            theLB.insert(tk.END,case_name)
        self.theLB = theLB
        #双击事件
        theLB.bind('<Double-Button-1>',self._reflush_case)
        theLB.bind('<Control-f>',self._open_excel)
        #for i in range(30):
        #    theLB.insert(tk.END,"Test_abcdefghjgl_00"+str(i))

    def _show_case_steps(self,text = "Steps",width = 340,height = 520):
        py_frame2 = tk.LabelFrame(self.root_windows,text = "Steps",width = 340,height = 520)
        py_frame2.place(x=240,y=5)
        text=self.handle_case.get_current_case_detail()
        theLabel = tk.Label(py_frame2,width=45,height=27,text=text,wraplength = 300,justify = 'left',anchor = 'nw')
        theLabel.place(x=5,y=5)

    def _show_case_logs(self,text = "Logs",width = 340,height = 520):
        py_frame3 = tk.LabelFrame(self.root_windows,text = "Logs",width = 340,height = 520)
        py_frame3.place(x=590,y=5)
        context = self.handle_case.get_current_case_log()
        log_text = tk.Text(py_frame3,width=45,height=37)
        log_text.insert(tk.INSERT,context)
        log_text.place(x=5,y=5)
        #theLabel = tk.Label(py_frame3,width=45,height=27,text=context ,wraplength = 300,justify = 'left',anchor = 'nw')
        #theLabel.place(x=5,y=5)
        log_text.bind('<Control-f>',self._search_log)
        self.log_text = log_text


    def _show_case_result(self,text = "Result",width = 220,height = 520):
        py_frame4 = tk.LabelFrame(self.root_windows,text = "Result",width = 220,height = 520)
        py_frame4.place(x=940,y=5)
        result_text = tk.Text(py_frame4, width=28, height=37)
        result_text.place(x=5,y=5)
        self.result_text = result_text

    def _show_record_button(self):
        update_button1 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Record Result",width = 15, height = 2,command = self._record_result)
        update_button1.place(x = 1000 , y=535)

    def _show_import_button(self):
        update_button2 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Import Logs",width = 15, height = 2,command = self._import_log)
        update_button2.place(x = 710 , y=535)

    def _show_export_button(self):
        update_button3 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Export Excel",width = 15, height = 2,command = self._save_excel)
        update_button3.place(x = 360 , y=535)

    def _show_reflush_button(self):
        ##已废弃
        update_button3 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Reflush Case",width = 15, height = 2,command = self._reflush_case)
        update_button3.place(x = 60 , y=535)
        #self.py_text = tk.Text(self.py_frame, width = 190, height = 490,bg="whitesmoke")
        #py_text = self.py_text
        #py_text.place(x=5,y=5)

    def _reflush_case(self,event):
        ##根据选择的caseName 刷新step，log
        case_index = self.theLB.curselection()
        print(case_index)
        if case_index[0]:
            print(case_index)
            self.handle_case.set_index(case_index[0])
            ##没必要完全重画，待优化
            self._show_case_steps()
            self._show_case_logs()
            self.result_text.delete("0.0","end")

    def _record_result(self):
        ##记录用户数输入的result
        context = self.result_text.get("0.0","end")
        self.handle_case.set_current_case_result(context)
        #self.result_text.delete("0.0","end")

    def _import_log(self):
        ##通过文件管理器导入log文件,指定初始目录
        log_path = filedialog.askopenfilename(initialdir="D:\\python_demo\\Hamster\\")
        print(log_path)
        self.handle_case.set_current_log(log_path)
        self._show_case_logs()

    def _open_excel(self):
        pass
    '''
        ##通过文件管理器导入case文件,指定初始目录
        log_path = filedialog.askopenfilename(initialdir="D:\\python_demo\\Hamster\\")
        print(log_path)
        self.handle_case.set_current_log(log_path)
        self._show_case_logs()
    '''
    def _save_excel(self):
        ##目前写死路径，后面改为时间戳形式的路径
        ##或者用户选择保存在哪里
        export_path = filedialog.asksaveasfilename(defaultextension='.xls')
        print(export_path)
        self.handle_case.export_case_to_excel(export_path)

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

    def run_windows(self):
        self._show_case_list()
        self._show_case_steps()
        self._show_case_logs()
        self._show_case_result()
        self._show_export_button()
        self._show_import_button()
        self._show_reflush_button()
        self._show_record_button()
        tk.mainloop()

    def func_update(self):
        ##已废弃
        pass


if __name__ == '__main__':
    config = ConfigLoad()
    print(config.get("windows","size"))
    windows = HandleWindows(config)
    windows.run_windows()
