import os

from matersdk.io.publicLayer.structure import DStructure


class StructureFileConvertorFrompw(object):
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
        def get_structure_file_name(current_path:str=current_path):
            input_file_name = input("结构文件名 (default: atom.config)\n------------>>\n")
            if (input_file_name == ""):
                input_file_name = "atom.config"
            input_file_path = os.path.join(current_path, input_file_name)

            return input_file_path
        
        
        ### Step 2. 转换
        ### Step 2.1. 根据输入设置格式、输出文件
        if (structure_file_convert_choice == "1"):
            input_file_path:str = get_structure_file_name(
                                        structure_file_convert_choice=structure_file_convert_choice,
                                        current_path=current_path)
            input_file_format:str = "pwmat"
            output_file_path:str = os.path.join(current_path, "POSCAR")
            output_file_format:str = "poscar"
        
        if (structure_file_convert_choice == "2"):
            input_file_path:str = get_structure_file_name(
                                        structure_file_convert_choice=structure_file_convert_choice,
                                        current_path=current_path)
            input_file_format:str = "pwmat"
            output_file_path:str = os.path.join(current_path, "atom.xsf")
            output_file_format:str = "xsf"
        
        if (structure_file_convert_choice == "3"):
            input_file_path:str = get_structure_file_name(
                                        structure_file_convert_choice=structure_file_convert_choice,
                                        current_path=current_path)
            input_file_format:str = "pwmat"
            output_file_path:str = os.path.join(current_path, "rndstr.in")
            output_file_format:str = "atat"
        
        if (structure_file_convert_choice == "4"):
            input_file_path:str = get_structure_file_name(
                                        structure_file_convert_choice=structure_file_convert_choice,
                                        current_path=current_path)
            input_file_format:str = "pwmat"
            output_file_path:str = os.path.join(current_path, "atom.cif")
            output_file_format:str = "cif"

        if (structure_file_convert_choice == "5"):
            print("Under Development!!!")
            
        if (structure_file_convert_choice == "6"):
                print("Under Development!!!")    
        
        
        