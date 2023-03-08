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
from .etotWriter import EtotWriter


class EtotWriterMain(object):
    def __init__(self,
                task_str:str,
                atom_config_path:str,
                ):
        '''
        Parameters
        ----------
            1. `task_str`: str
                - 任务的mark (简写), e.g. `SC`
            2. atom_config_path: 
                - 相对路径，e.g. `atom.config`
        '''
        self.task_str = task_str
        self.etot_writer = EtotWriter(
                        atom_config_name=atom_config_path,
                        )
    
    def execute():
        pass
    
    
    #def write_task(self):
    #   if self.task_str 
    #    self.etot_writer.write_task(task_name=self.task_str)

    


if __name__ == "__main__":
    
    task_str = sys.argv[1]  # 任务类型的大写 -- e.g. SC
    long_str = sys.argv[2]  # 完整的输入 `e.g. scpesgsp`
    current_path = os.getcwd()
    atom_config_path = os.path.join(current_path, sys.argv[3])  # atom.config 的路径
    
    etot_writer_main = EtotWriterMain(
                            task_str=task_str,
                            atom_config_path=atom_config_path,
    )
    
    