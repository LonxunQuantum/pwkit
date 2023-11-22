from abc import abstractmethod
import os
import sys
from typing import Union

class UITemplate(object):
    @abstractmethod
    def show(self):
        ### Part I.
        print("{0:-^60}".format(" xxxx "))
        print(
''' 1) xxx                      2) xxx
 3) xxx                     4) xxx
'''
        )        
        
        ### Part II. Exit
        print(
'''
 bb) 返回上一级目录
 q)  退出'''
        )
    
    
    @abstractmethod
    def process_input(self):
        back_mark:Union[None, str] = None

        while (True):
            if (back_mark == "BB"):
                self.show()
            user_choice:str = input("------------>> \n").upper()
            
            # Case 1. Exit the program
            if (user_choice == "Q"):
                try:
                    sys.exit()
                except SystemExit as e:
                    break
            
            elif (user_choice == "1"):
                # submenu.show()
                # back_mark = submenu.process_input()
                # if (back_mark == None)
                #    break
                # elif (back_mark == "BB")
                #    continue
                pass
            
            else:
                print("(*_*) Unsupported input! Try again... (*_*)")
            
    
    
    
class OPTTemplate(object):
    @abstractmethod
    def run(self):
        pass