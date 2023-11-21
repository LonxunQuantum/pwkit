import sys 


class UtilityUI(object):
    def show(self):
        ### Part I. Utility 数据可视化
        print("{0:-^60}".format(" 数据可视化 "))
        print(
''' 1) 电荷密度可视化        2) 波函数可视化        3) 态密度图绘制
 4) 能带图绘制     
'''
        )

    ### Part II. Utility 数据后处理
        print("{0:-^60}".format(" 数据后处理 "))
        print(
''' a) 能带带隙              b) 真空能级
'''
        )

    ### Part V. EXIT
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
        while (True): # Reinput when user unsupported selection
            utility_ui_choice = input("------------>> \n").upper()
            
            # Case 1. Exit the program
            if (utility_ui_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    break
            
            elif (utility_ui_choice == "BB"):
                return "BB"

            elif (utility_ui_choice == "1"):
                print("Under Development!!!")
                break
            
            elif (utility_ui_choice == "2"):
                print("Under Development!!!")
                break
                
            elif (utility_ui_choice == "3"):
                print("Under Development!!!")
                break
            
            elif (utility_ui_choice == "4"):
                print("Under Development!!!")
                break
            
            elif (utility_ui_choice == "A"):
                print("Under Development!!!")
                break
            
            elif (utility_ui_choice == "B"):
                print("Under Development!!!")
                break