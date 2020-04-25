#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import sys,os
sys.path.append(os.path.abspath('../config/'))
print(os.path.abspath('../config/'))
from config_load import ConfigLoad

class HandleWindows(object):

    def __init__(self,cfg):
        size = cfg.get("windows","size")
        self.root_windows = tk.Tk()
        self.root_windows.title("")
        self.root_windows.geometry("1170x600")
        self.py_frame1 = tk.LabelFrame(self.root_windows,text = "Case List",width = 220,height = 520)
        self.py_frame1.place(x=10,y=5)
        theLB = tk.Listbox(self.py_frame1, selectmode=tk.SINGLE,width = 28, height=27)
        theLB.place(x=5,y=5)
        for i in range(30):
            theLB.insert(tk.END,"Test_abcdefghjgl_00"+str(i))
        self.py_frame2 = tk.LabelFrame(self.root_windows,text = "Steps",width = 340,height = 520)
        self.py_frame2.place(x=240,y=5)
        text="为了获得龙泪，狼进入源之宫皇宫后在山顶的祭祀台发现巫女，检查佛坛后场景变换" \
             "(应该和仙峰寺正殿到幻境的原理相同)，此时第一阶段是一群龙树仙翁，他们应该已经是樱龙的一" \
             "部分，而根据其形态推测这些树人可能是已经被樱龙同化吸收了生命力的淤加美族男性，被狼" \
             "破坏后樱龙暴怒，狼击败樱龙后获得其眼泪。"
        theLabel = tk.Label(self.py_frame2,width=45,height=27,text=text,wraplength = 300,justify = 'left',anchor = 'nw')
        theLabel.place(x=5,y=5)
        self.py_frame3 = tk.LabelFrame(self.root_windows,text = "Logs",width = 340,height = 520)
        self.py_frame3.place(x=590,y=5)
        theLabel = tk.Label(self.py_frame3,width=45,height=27,text="No log",wraplength = 300,justify = 'left',anchor = 'nw')
        theLabel.place(x=5,y=5)
        self.py_frame4 = tk.LabelFrame(self.root_windows,text = "Result",width = 220,height = 520)
        self.py_frame4.place(x=940,y=5)
        text = tk.Text(self.py_frame4, width=28, height=37)
        text.place(x=5,y=5)
        update_button1 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Record Result",width = 15, height = 2,command = self.func_update)
        update_button1.place(x = 1000 , y=535)

        update_button2 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Import Logs",width = 15, height = 2,command = self.func_update)
        update_button2.place(x = 710 , y=535)

        update_button3 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Export Excel",width = 15, height = 2,command = self.func_update)
        update_button3.place(x = 360 , y=535)

        update_button3 = tk.Button(self.root_windows,bg = 'whitesmoke',text="Reflush Case",width = 15, height = 2,command = self.func_update)
        update_button3.place(x = 60 , y=535)
        #self.py_text = tk.Text(self.py_frame, width = 190, height = 490,bg="whitesmoke")
        #py_text = self.py_text
        #py_text.place(x=5,y=5)
        tk.mainloop()

    def func_update(self):
        pass


if __name__ == '__main__':
    config = ConfigLoad()
    print(config.get("windows","size"))
    windows = HandleWindows(config)
