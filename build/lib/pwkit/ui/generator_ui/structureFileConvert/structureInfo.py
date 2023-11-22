import os
import sys
import subprocess
from typing import Union, Tuple
from matersdk.io.publicLayer.structure import DStructure
    
from ...ui_template import UITemplate
from ....variable import *


class StructureInfo(UITemplate):
    def show(self):
        print("{0:-^50}".format(" 查看结构信息 "))
        print(
''' 1) 查看结构信息
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
                
                ### 输出信息
                ### 1. 晶格基矢
                basis_vector_array = structure.lattice.matrix
                print("*{0:-^72}*".format(" Output "))
                print("\t* 晶胞的基矢(单位:埃) :")
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "a1",
                        round(basis_vector_array[0][0], 4),
                        round(basis_vector_array[0][1], 4),
                        round(basis_vector_array[0][2], 4)
                        )
                )
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "a2",
                        round(basis_vector_array[1][0], 4),
                        round(basis_vector_array[1][1], 4),
                        round(basis_vector_array[1][2], 4)
                        )
                )
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "a3",
                        round(basis_vector_array[2][0], 4),
                        round(basis_vector_array[2][1], 4),
                        round(basis_vector_array[2][2], 4)
                        )
                )
                
                ### 2. 倒易晶格基矢
                print("\t* 倒易晶胞的基矢(单位:2pi/埃) :")
                reciprocal_basis_vector_array = structure.lattice.reciprocal_lattice_crystallographic.matrix
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "b1",
                        round(reciprocal_basis_vector_array[0][0], 4),
                        round(reciprocal_basis_vector_array[0][1], 4),
                        round(reciprocal_basis_vector_array[0][2], 4)
                        )
                )
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "b2",
                        round(reciprocal_basis_vector_array[1][0], 4),
                        round(reciprocal_basis_vector_array[1][1], 4),
                        round(reciprocal_basis_vector_array[1][2], 4)
                        )
                )
                print("\t\t{0:<10}{1:<15}{2:<15}{3:<15}".format(
                        "b3",
                        round(reciprocal_basis_vector_array[2][0], 4),
                        round(reciprocal_basis_vector_array[2][1], 4),
                        round(reciprocal_basis_vector_array[2][2], 4)
                        )
                )  
                
                ### 3. 体积
                print("\t* 晶胞的体积(单位:埃^3) : ", structure.volume)
                
                ### 4. 基矢长度、夹角
                basis_vector_lengths:Tuple[float] = structure.lattice.abc
                print("\t* 晶胞基矢的长度(单位:埃) :")
                print("\t\t{0:<15}{1:<15}{2:<15}".format("a1-length", "a2-length", "a3-length"))
                print("\t\t{0:<15}{1:<15}{2:<15}".format(
                                                    round(basis_vector_lengths[0], 8),
                                                    round(basis_vector_lengths[1], 8),
                                                    round(basis_vector_lengths[2], 8)
                                                )
                )
                print("\t* 晶胞基矢的夹角(单位:度) :")
                angles:Tuple[float] = structure.lattice.angles
                print("\t\t{0:<15}{1:<15}{2:<15}".format("alpha", "beta", "gamma"))
                print("\t\t{0:<15}{1:<15}{2:<15}".format(
                    round(angles[0], 2),
                    round(angles[1], 2),
                    round(angles[2], 2)
                    )
                )
                
                print("*{0:-^72}*".format(""))
                break
                
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")