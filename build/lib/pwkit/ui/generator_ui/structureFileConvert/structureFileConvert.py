import os

from matersdk.io.publicLayer.structure import DStructure


class StructureFileConvertor(object):
    @staticmethod
    def convert(
            input_file_path:str, 
            input_file_format:str,
            output_file_path:str,
            output_file_format:str):
        structure = DStructure.from_file(file_path=input_file_path, file_format=input_file_format)
        structure.to(file_path=output_file_path, file_format=output_file_format)
    
    @staticmethod
    def show():
        print("{0:-^50}".format("  其他格式 -> PWMat格式"))
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
        
        
    @staticmethod
    def process_input():
        '''
        Description
        -----------
            1. 
        '''
        current_path = os.getcwd()
        
        ### Step 1. 读取用户的输入
        ### Step 1.1. 选项
        structure_file_convert_choice = input("------------>>\n")
        
        
        ### Step 1.2. 输入文件名
        input_file_name = input("结构文件名 (default: 'atom.config')\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
        
        if not os.path.exists(input_file_path):
            raise FileNotFoundError("{0} doesn't exist!!!".format(input_file_name))
        
        ### Step 2. 转换
        ### Step 2.1. 根据输入设置格式、输出文件
        if (structure_file_convert_choice == "1"):
            input_file_format = "poscar"
            output_file_path = os.path.join(current_path, "atom.config")
            output_file_format = "pwmat"
        
        elif (structure_file_convert_choice == "2"):
            input_file_format = "xsf"
            output_file_path = os.path.join(current_path, "atom.config")
            output_file_format = "pwmat"
        
        elif (structure_file_convert_choice == "3"):
            input_file_format = "atat"
            output_file_path = os.path.join(current_path, "atom.config")
            output_file_format = "pwmat"
            
        elif (structure_file_convert_choice == "4"):
            input_file_format = "cif"
            output_file_path = os.path.join(current_path, "atom.config")
            output_file_format = "pwmat"
            
        elif (structure_file_convert_choice == "5"):
            input_file_format = "pwscf"
            print("Under Development!")
        
        elif (structure_file_convert_choice == "6"):
            input_file_format = "cell"
            print("Under Development!")
            
        elif (structure_file_convert_choice == "7"):
            input_file_format = "pdb"
            print("Under Development!")
            
        elif (structure_file_convert_choice == "8"):
            input_file_format = "inp"
            print("Under Development!")
        
        elif (structure_file_convert_choice == "9"):
            input_file_format = "outcar"
            print("Under Development!")
        
        
        StructureFileConvertor.convert(
                        input_file_path=input_file_path,
                        input_file_format=input_file_format,
                        output_file_path=output_file_path,
                        output_file_format=output_file_format)
        
        