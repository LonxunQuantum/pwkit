import os 
import sys



class EtotWriter(object):
    '''
    Description
    -----------
        1. `EtotWriter` 是一个 `BaseClass`，我们将在其他文件中调用
            这个类，逐行写入 `etot.input`
    '''
    def __init__(self,
                etot_path:str=os.path.join(os.getcwd(), "etot.input"),
                ):
        self.etot_path = etot_path
        
        if os.path.exists(self.etot_path):
            os.remove(self.etot_path)
    
    
    def write_task(self):
        job_task = sys.argv[1]
        
        with open(self.etot_path, "a") as f:
            f.write("JOB = {0}".format(job_task))
    
    
    def write_functional(self):
        pass
    
    
    def write_pseudo(self):
        pass
    
    
    def write_specific(self):
        pass