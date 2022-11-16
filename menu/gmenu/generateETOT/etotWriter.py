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
        task_name = sys.argv[1]
        
        with open(self.etot_path, "a") as f:
            f.write("JOB = {0}\n".format(task_name))
    
    
    def write_functional(self):
        functional_name = sys.argv[1]
        
        with open(self.etot_path, "a") as f:
            f.write("XCFUNCTIONAL = {0}\n".format(functional_name))      
    
    
    def write_pseudo(self):
        pass
    
    
    def write_specific(self):
        pass