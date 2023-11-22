import os
import sys
import subprocess
from typing import Union
from matersdk.io.publicLayer.structure import DStructure

from ...ui_template import UITemplate
from ....variable import *


class StructureFileConvertorFrompw(UITemplate):
    def convert(
            self,
            input_file_path:str,
            input_file_format:str,
            output_file_path:str,
            output_file_format:str):
        structure = DStructure.from_file(file_path=input_file_path, file_format=input_file_format)
        structure.to(file_path=output_file_path, file_format=output_file_format)
    
    
    def show(self):
        print("{0:-^50}".format(" PWmat格式 -> 其他格式 "))
        print(
''' 1) atom.config -> POSCAR文件 (POSCAR)    
 2) atom.config -> xsf文件    (atom.xsf)
 3) atom.config -> atat文件   (rndstr.in)
 4) atom.config -> cif文件    (atom.cif)
 5) MOVEMENT    -> xsf文件    (MOVEMENT.xsf)
 6) MOVEMENT    -> xyz文件    (MOVEMENT.xyz)
'''
        )
        
        print(
'''
 bb) 返回上一级目录
 q) 退出'''
        )
        
    
    def process_input(self):
        '''
        Description
        -----------
            1. 
        '''
        current_path = os.getcwd()
        # back_mark:Union[None, str] = None
        
        while (True):
            ### Step 1. 读取用户的输入
            ### Step 1.1. 选项
            structure_file_convert_choice = input("------------>>\n").upper()
            
            ### Step 2. 转换
            ### Step 2.1. 根据输入设置格式、输出文件
            if (structure_file_convert_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    pass
            
            elif (structure_file_convert_choice == "BB"):
                return "BB"
            
            elif (structure_file_convert_choice == "1"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_path:str = os.path.join(current_path, "POSCAR")
                output_file_format:str = "poscar"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
            
            elif (structure_file_convert_choice == "2"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_path:str = os.path.join(current_path, "atom.xsf")
                output_file_format:str = "xsf"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
            
            elif (structure_file_convert_choice == "3"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_path:str = os.path.join(current_path, "rndstr.in")
                output_file_format:str = "atat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
            
            elif (structure_file_convert_choice == "4"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_path:str = os.path.join(current_path, "atom.cif")
                output_file_format:str = "cif"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break

            elif (structure_file_convert_choice == "5"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_format:str = "xsf"
                convert_from_config_x = os.path.join(PWKIT_SCRIPT_DIR, "generator_scripts", "structureFileConvert_scripts", "convert_from_config.x")
                subprocess.call([convert_from_config_x, input_file_path])
                break
                
            elif (structure_file_convert_choice == "6"):
                input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
                if (input_file_name == ""):
                    input_file_name = "atom.config"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwmat"
                output_file_format:str = "xyz"
                convert_from_config_x = os.path.join(PWKIT_SCRIPT_DIR, "generator_scripts", "structureFileConvert_scripts", "convert_from_config.x")
                subprocess.call([convert_from_config_x, input_file_path])
                break
        
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")
            