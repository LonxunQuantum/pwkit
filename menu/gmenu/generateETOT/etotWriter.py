#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os 
import sys


class EtotWriter(object):
    '''
    Description
    -----------
        1. `EtotWriter` 是一个 `BaseClass`，我们将在其他文件中调用
            这个类，逐行写入 `etot.input`
    
    Attributions
    ------------
        1. `self.write_task()`: 写入 `任务类型`
        2. `self.write_functional()`: 写入 `泛函设置`
        3. `self.write_pseudo()`: 写入 `赝势设置`
        4. `self.write_specific()`: 写入 `特殊设置`
    '''
    def __init__(self,
                etot_path:str=os.path.join(os.getcwd(), "etot.input"),
                ):
        self.etot_path = etot_path
        
        #if os.path.exists(self.etot_path):
        #    os.remove(self.etot_path)
    
    
    def write_task(self):
        '''
        Description
        -----------
            1. run in `1_write_task.py` file
        '''
        setattr(self, "task_name", sys.argv[1])
        
        with open(self.etot_path, "a") as f:
            f.write("1  4\n\n")
            f.write("#基础设置\n")
            f.write("JOB = {0}\n".format(self.task_name))
    
    
    def write_functional(self):
        '''
        Description
        -----------
            1. run in `2_write_functional.py` file
        '''
        setattr(self, "functional_name", sys.argv[1])
        
        with open(self.etot_path, "a") as f:
            f.write("XCFUNCTIONAL = {0}\n".format(self.functional_name))
    
    
    def write_accuracy(self):
        '''
        Description
        -----------
            1. 
        '''
        if self.task_name == "SC":
            accuracy = "NORM"
            convergence = "EASY"
            precision = "AUTO"
        
        with open(self.etot_path, "a") as f:
            f.write("ACCURACY = {0}\n".format(accuracy))
            f.write("CONVERGENCE = {0}\n".format(convergence))
            f.write("PRECISION = {0}\n".format(precision))
    
    
    def write_scf(self):
        if self.task_name == "SC":
            ecut = 50
            mp_n123 = "12 12 1 0 0 0 0"
            scf_iter0_1 = "6 4 3 0.0 0.0025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
        
        with open(self.etot_path, "a") as f:
            f.write("\n\n")
            f.write("#电子自洽设置\n")
            f.write("Ecut = {0}\n".format(ecut))
            f.write("MP_N123 = {0}\n".format(mp_n123))
            f.write("SCF_ITER0_1 = {0}\n".format(scf_iter0_1))
            f.write("SCF_ITER0_2 = {0}\n".format(scf_iter0_2))
    
    
    def write_specific(self):
        specific_name = sys.argv[1]
        
        # 首次写入 "#特殊设置\n" 
        mark = False
        with open(self.etot_path, "r") as f:
            rows_content = f.readlines()
            if "#特殊设置\n" not in rows_content:
                mark = True
        
        # 写入 PWmat 的选项
        with open(self.etot_path, "a") as f:    
            if mark == True:
                f.write("\n\n")
                f.write("#特殊设置\n")              
            # 1. 自旋极化
            if (specific_name == "SP"):
                f.write("SPIN = 1\n")
            # 2. 自旋轨道耦合
            # 3. 非共线磁矩+自旋轨道耦合
            # 4. 带电体系
            # 5. DFT+U
            # 6. DFT+D3
            # 7. 固定电势计算
            # 8. 溶剂效应
            
        pass
    
    
    def write_pseudo(self):
        pass