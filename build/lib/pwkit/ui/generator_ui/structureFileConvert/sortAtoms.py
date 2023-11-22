import os 
import sys
import subprocess
from typing import Union, Tuple
from matersdk.io.publicLayer.structure import DStructure

from ...ui_template import UITemplate
from ....variable import *


class AtomsSorter(UITemplate):
    def show(self):
        print("{0:-^50}".format(" 原子排序 "))
        print(
''' 1) 按原子序数从小到大排序
'''
        )
        print(
'''
 bb) 返回上一级目录
 q) 退出'''
        )
        
        
    def process_input(self):
        current_path = os.getcwd()
        
        while (True):
            ### Step 1. 读取用户的输入
            user_choice = input("------------>>\n").upper()

            ### Step 2. run
            if (user_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    pass
            
            elif (user_choice == "BB"):
                return "BB"
            
            elif (user_choice == "1"):
                print("输入atom.config格式的文件名 (default: atom.config)")
                file_name = input("------------>>\n")
                if file_name == "":
                    file_name = "atom.config"
                file_path = os.path.join(current_path, file_name)
                structure = DStructure.from_file(
                        file_format="pwmat",
                        file_path=file_path
                )
                
                ### 原子按照原子序数排序
                structure.reformat_elements_()
                structure.to(file_path=file_path, file_format="pwmat")
                break
            
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")
            