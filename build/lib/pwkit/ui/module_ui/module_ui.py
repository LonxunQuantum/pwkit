import sys


class ModuleUI(object):
    def show(self):
        ### Part I. 物质结构
        print("{0:-^60}".format(" 物质结构 "))
        print(
''' 1) 结构搜索                2) 无序结构
 3) 分子动力学数据处理      4) CIF 文件转换与结构处理
'''
        )
        
        ### Part II. 电子结构及声子计算
        print("{0:-^55}".format(" 电子结构及声子计算 "))
        print(
''' 5) 电子结构                6) 声子计算
'''
        )
        
        ### Part III. 电子结构及声子计算
        print("{0:-^53}".format(" 光、磁、力学和极化性质 "))
        print(
''' 7) 光学性质                8) 磁学性质
 9) 力学性质                a) 极化性质
'''
        )
        
        ### Part IV. 其他模块
        print(
''' b) 缺陷性质                c) 电化学性质
 d) 输运性质                e) 超快动力学过程
 f) Beyond DFT              g) 电子束辐照分解
 h) 大体系计算              i) 机器学习力场
 j) 其它
'''
        )
        
        ### Part V. EXIT
        print(
'''
 bb) 返回上一级目录
 q)  退出
'''
        )
        
        
    def process_input(self):
        ### User input choice
        '''
        Note: In pwkit, we convert all input to upper case.
        '''
        while (True): # Reinput when user unsupported selection
            module_ui_choice = input("------------>> \n").upper()
            
            # Case 1. Exit the program
            if (module_ui_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    break
            
            elif (module_ui_choice == "BB"):
                return "BB"

            # 结构搜索 
            elif(module_ui_choice == "1"):
                print("Under Development !!!")
                break
            
            # 无序结构
            elif(module_ui_choice == "2"):
                print("Under Development !!!")
                break
            
            # 分子动力学数据处理
            elif(module_ui_choice == "3"):
                print("Under Development !!!")
                break
            
            # CIF 文件转换与结构处理
            elif(module_ui_choice == "4"):
                print("Under Development !!!")
                break
            
            # 电子结构
            elif(module_ui_choice == "5"):
                print("Under Development !!!")
                break
            
            # 声子计算
            elif(module_ui_choice == "6"):
                print("Under Development !!!")
                break
            
            # 光学性质
            elif(module_ui_choice == "7"):
                print("Under Development !!!")
                break
            
            # 磁学性质
            elif(module_ui_choice == "8"):
                print("Under Development !!!")
                break
            
            # 力学性质
            elif(module_ui_choice == "9"):
                print("Under Development !!!")
                break
            
            # 极化性质
            elif(module_ui_choice == "A"):
                print("Under Development !!!")
                break
            
            # 缺陷性质
            elif(module_ui_choice == "B"):
                print("Under Development !!!")
                break
            
            # 电化学性质
            elif(module_ui_choice == "C"):
                print("Under Development !!!")
                break
            
            # 输运性质
            elif(module_ui_choice == "D"):
                print("Under Development !!!")
                break
            
            # 超快动力学过程
            elif(module_ui_choice == "E"):
                print("Under Development !!!")
                break
            
            # Beyond DFT
            elif(module_ui_choice == "F"):
                print("Under Development !!!")
                break
            
            # 电子束辐照分解
            elif(module_ui_choice == "G"):
                print("Under Development !!!")
                break
            
            # 大体系计算
            elif(module_ui_choice == "H"):
                print("Under Development !!!")
                break
            
            # 机器学习力场
            elif(module_ui_choice == "I"):
                print("Under Development !!!")
                break
            
            # 其它
            elif(module_ui_choice == "J"):
                print("Under Development !!!")
                break