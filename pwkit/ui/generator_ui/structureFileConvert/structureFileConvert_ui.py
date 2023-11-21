import sys
from typing import Union

from ...ui_template import UITemplate
from .structureFileConvert_topw import StructureFileConvertorTopw
from .structureFileConvert_frompw import StructureFileConvertorFrompw


class StructureFileConvertUI(UITemplate):
    def show(self):
        ### Part I. 
        print("{0:-^60}".format(" 结构转换 "))
        print(
''' 1) 其他格式 -> PWMat格式        2) PWMat格式 -> 其他格式
 3) 查看结构信息                 4) 按照原子序数整理atom.config
'''
        )
        
        ### Part . EXIT
        print(
'''
bb) 返回上一级目录
q)  退出'''
        )
    
    
    def process_input(self):
        ### User input choice
        '''
        Note: In pwkit, we convert all input to upper case
        '''
        back_mark:Union[None, str] = None
        
        while (True): # Reinput when user input unsupported selection.
            if (back_mark == "BB"):
                self.show()
            user_choice:str = input("------------>> \n").upper()
            
            # Case 1. Exit the program
            if (user_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    break
            
            elif (user_choice == "BB"):
                return "BB"
            
            # Case 2. 1) 其他格式 -> PWmat 格式
            elif (user_choice == "1"):
                StructureFileConvertorTopw().show()
                back_mark = StructureFileConvertorTopw().process_input()
                if back_mark == None:
                    break
                elif back_mark == "BB":
                    return "BB"
            
            # Case 3. 2) PWmat 格式 -> 其他格式
            elif (user_choice == "2"):
                StructureFileConvertorFrompw().show()
                back_mark = StructureFileConvertorFrompw().process_input()
                if back_mark == None:
                    break
                elif back_mark == "BB":
                    return "BB"
            
            # Case 4. 3) 生成高对称点文件
            elif (user_choice == "3"):
                print("Under development")
                break
            
            # Case 5. 4) 外加电场
            elif (user_choice == "4"):
                print("Under development")
                break
            
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")