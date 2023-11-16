import sys


class GeneratorUI(object):
    def show(self):
        ### Part I. 物质结构
        print("{0:-^60}".format(" 生成输入文件 "))
        print(
''' 1) 生成etot.input                2) 结构文件格式转换
 3) 生成高对称点文件              4) 外加电场
'''
        )
        
        ### Part II. Exit
        print(
'''
 bb) 返回上一级目录
 q)  退出'''
        )
        
        
    def process_input(self):
        ### User input choice
        '''
        Note: In pwkit, we convert all input to upper case.
        '''
        while (True): # Reinput when user input unsupported selection.
            generator_ui_choice = input("------------>> \n").upper()
            
            # Case 1. Exit the program
            if (generator_ui_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    break
                
            elif (generator_ui_choice == "BB"):
                return "BB"
                
            # Case 2. 1) 生成etot.input
            elif (generator_ui_choice == "1"):
                print("Under Development !!!")
                break
            
            # Case 3. 2) 结构文件格式转换
            elif (generator_ui_choice == "2"):
                print("Under Development !!!")
                break
            
            # Case 4. 3) 生成高对称点文件
            elif (generator_ui_choice == "3"):
                print("Under Development !!!")
                break
            
            # Case 5. 4) 外加电场
            elif (generator_ui_choice == "4"):
                print("Under Development !!!")
                break