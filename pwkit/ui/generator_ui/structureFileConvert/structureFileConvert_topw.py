import os
import sys
import subprocess
from typing import Union
from matersdk.io.publicLayer.structure import DStructure

from ...ui_template import UITemplate
from ....variable import *


class StructureFileConvertorTopw(UITemplate):
    def convert(
            self,
            input_file_path:str, 
            input_file_format:str,
            output_file_path:str,
            output_file_format:str):
        structure = DStructure.from_file(file_path=input_file_path, file_format=input_file_format)
        structure.to(file_path=output_file_path, file_format=output_file_format)
    
    
    def show(self):
        print("{0:-^50}".format(" 其他格式 -> PWMat格式 "))
        print(
''' 1) POSCAR文件 (POSCAR)     -> atom.config
 2) xsf文件    (atom.xsf)   -> atom.config
 3) atat文件   (rndstr.in)  -> atom.config     
 4) cif文件    (atom.cif)   -> atom.config     
 5) pwscf文件  (atom.pwscf) -> atom.config     
 6) cell文件   (atom.cell)  -> atom.config
 7) pdb文件    (atom.pdb)   -> atom.config   (Under Development)
 8) inp文件    (atom.inp)   -> atom.config
 9) OUTCAR文件 (OUTCAR)     -> MOVEMENT
'''
        )
        print(
'''
bb) 返回上一级目录
q)  退出'''
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
            
            ### Step 2. 处理用户输入
            ### Step 2.1. 处理 user_choice
            if (structure_file_convert_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    pass
            
            elif (structure_file_convert_choice == "BB"):
                return "BB"
        
            elif (structure_file_convert_choice == "1"):
                ### Step 2.2. 处理 input_file_name
                input_file_name = input("结构文件名 (default: POSCAR)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "POSCAR"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format:str = "poscar"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
            
            elif (structure_file_convert_choice == "2"):
                input_file_name:str = input("结构文件名 (default: atom.xsf)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.xsf"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "xsf"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
                        
            elif (structure_file_convert_choice == "3"):
                input_file_name:str = input("结构文件名 (default: rndstr.in)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "rndstr.in"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "atat"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
                            
            elif (structure_file_convert_choice == "4"):
                input_file_name:str = input("结构文件名 (default: atom.cif)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.cif"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "cif"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
                            
            elif (structure_file_convert_choice == "5"):
                input_file_name:str = input("结构文件名 (default: atom.pwscf)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.pwscf"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "pwscf"
                pwscf2config_x_path:str = os.path.join(PWKIT_SCRIPT_DIR, "generator_scripts", "structureFileConvert_scripts", "pwscf2config.x")
                subprocess.call([pwscf2config_x_path, "<", input_file_path])
                break
            
            elif (structure_file_convert_choice == "6"):
                input_file_name:str = input("结构文件名 (default: atom.cell)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.cell"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format = "cell"
                cell2config_x_path:str = os.path.join(PWKIT_SCRIPT_DIR, "generator_scripts", "structureFileConvert_scripts", "cell2config.x")
                subprocess.call([cell2config_x_path, "<", input_file_path])
                break
                
            elif (structure_file_convert_choice == "7"):
                input_file_name:str = input("结构文件名 (default: atom.pdb)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.pdb"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "pdb"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
                
            elif (structure_file_convert_choice == "8"):
                input_file_name:str = input("结构文件名 (default: atom.inp)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "atom.inp"
                input_file_path:str = os.path.join(current_path, input_file_name)
                input_file_format:str = "inp"
                output_file_path:str = os.path.join(current_path, "atom.config")
                output_file_format:str = "pwmat"
                self.convert(
                    input_file_path=input_file_path,
                    input_file_format=input_file_format,
                    output_file_path=output_file_path,
                    output_file_format=output_file_format)
                break
            
            elif (structure_file_convert_choice == "9"):
                input_file_name:str = input("结构文件名 (default: OUTCAR)\n------------>>\n")
                if input_file_name == "":
                    input_file_name = "OUTCAR"
                input_file_path = os.path.join(current_path, input_file_name)
                input_file_format = "outcar"
                outcar2movement_py_path = os.path.join(PWKIT_SCRIPT_DIR, "generator_scripts", "structureFileConvert_scripts", "outcar2movement.py")
                subprocess.call(["python", outcar2movement_py_path])
                break
            
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")
                continue
            