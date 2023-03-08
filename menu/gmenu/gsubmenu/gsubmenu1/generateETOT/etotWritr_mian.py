'''
Description
-----------
    1. Optimizer
    2. 文件作用等效于
        - 1_xxx.py ~ 7_xxx.py
'''
import os
import sys
import subprocess
from etotWriter import EtotWriter
from select_task import *
from select_functional import *
from select_pseudo import *
from select_specific import *


class EtotWriterMain(object):
    def __init__(self,
                long_str:str,
                atom_config_path:str,
                density:float
                ):
        '''
        Parameters
        ----------
            1. `task_str`: str
                - 任务的mark (简写), e.g. `SC`
            2. atom_config_path: 
                - 相对路径，e.g. `atom.config`
        '''
        self.long_str = long_str
        self.etot_writer = EtotWriter(
                        atom_config_name=atom_config_path,
                        )
        self.density = density
    
    
    def execute(self):
        self.write_task()
        self.write_functional()
    
    
    def write_task(self):
        '''
        Description
        -----------
            1. 
        '''
        ### Step 1. 得到前两个字符，作为 `task_str`
        p1 = subprocess.Popen(
                        ["echo", "{0}".format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=True,
        )
        p1.wait()
        p2 = subprocess.Popen(
                        ["cut", "-c", "1-2"],
                        stdout=subprocess.PIPE,
                        shell=True,
        )
        output, _ = p2.communicate()
        task_str = output.decode()
        
        ### Step 2. `etot_writer` 赋予 `任务类型`
        task_str = select_task()
        if task_str in tasks_str_lst:
            self.etot_writer.write_task(task_name=task_str)
        #elif task_str == "default":     # menu.sh 文件中，在此之前已经处理过了! 
        #    raise SystemExit
        #else:                           # menu.sh 文件中，在此之前已经处理过了! 
        #    raise SystemExit
        
        
            ### Step 3. 在 `self.long_str` 删去任务类型
            p1 = subprocess.Popen(
                            ["echo", "{0}".format(self.long_str)],
                            stdout=subprocess.PIPE,
                            shell=True,
            )
            p1.wait()
            p2 = subprocess.Popen(
                            ["cut", "-c", "3-"]
            )
            output, _ = p2.communicate()
            self.long_str = output.decode()
        
        pp = subprocess.Popen(
                ["echo", "Part I. 任务类型设置成功.."],
                stdout=subprocess.PIPE,
                shell=True,                
        )
        pp.wait()
    
    
    def write_functional(self):
        '''
        Description
        -----------
            1. 
        '''
        ### Step 1. 得到 `self.long_str` 前两个字符，作为 `functional_str`
        p1 = subprocess.Popen(
                    ['echo', '{0}'.format(self.long_str)],
                    stdout=subprocess.PIPE,
                    shell=True,
        )
        p1.wait()
        p2 = subprocess.Popen(
                    ['cut', '-c', '1-2'],
                    stdout=subprocess.PIPE,
                    shell=True,
        )
        output, _ = p2.communicate()
        functional_str = output.decode()
        
        ### Step 2. `etot_writer` 赋予 `泛函类型`
        functional_str = select_functional(functional_str=functional_str)
        if functional_str == "default":
            self.etot_writer.write_functional(functional_name="PE")
        if functional_str in functionals_str_lst:
            self.etot_writer.write_functional(functional_name=functional_str)
        
            ### Step 3. 删去前两个代表 functional 的字符
            p1 = subprocess.Popen(
                        ['echo', '{0}'.format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=True
            )
            p1.wait()
            p2 = subprocess.Popen(
                        ['cut', '-c', '3-'],
                        stdout=subprocess.PIPE,
                        shell=True,
            )
            output, _ = p2.communicate()
            self.long_str = output.decode()
        print("Part II. 泛函类型设置成功..")
            
        
        
    def write_accuracy_and_scf(self):
        '''
        Description
        -----------
            1. 写入 ACCURACY 设置
                - Note: self.task=NS时，没有 density_in_2pi 变量
            2. 写入 电子自洽(scf) 设置
                - Note: self.task=NS时，没有 density_in_2pi 变量
        '''
        self.etot_writer.write_accuracy(density=self.density)
        self.etot_writer.write_scf(density=self.density)
    
    
    
    def write_pesudo(self):
        ### Step 1. 取出代表 `赝势类型` 的两个字符
        p1 = subprocess.Popen(
                    ['echo', '{0}'.format(self.long_str)],
                    stdout=subprocess.PIPE,
                    shell=True,
        )
        p1.wait()
        p2 = subprocess.Popen(
                    ['echo', '{0}'.format(self.long_str)],
                    stdout=subprocess.PIPE,
                    shell=True,
        )
        output, _ = p2.communicate()
        
        ### Step 2. 设置赝势类型，后面使用
        self.pseudo_str = output.decode()
        
        print("Part III. 赝势类型设置成功..")
    
    
    def write_specific(self):
        ### Step 1. 检查是否有剩余的字符，用于 `特殊设置`
        #if self.long_str == '':
            
        
        pass
        ### Step 2. 
        #self.write_specific()
            


if __name__ == "__main__":    
    long_str = sys.argv[1]  # 完整的输入 `e.g. scpesgsp`
    current_path = os.getcwd()
    atom_config_path = os.path.join(current_path, sys.argv[2])  # atom.config 的路径
    density = float(sys.argv[3])
    etot_writer_main = EtotWriterMain(
                            long_str=long_str,
                            atom_config_path=atom_config_path,
                            density=density,
    )
    
    
    etot_writer_main.execute()