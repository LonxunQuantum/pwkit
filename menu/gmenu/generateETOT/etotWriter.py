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
    
    
    def write_input_output(self):
        '''
        Note
        ---- 
            1. 内部包含写入赝势文件 `IN.PSP1`, `IN.PSP2`, ...
        '''
        ### Part I. 根据赝势类型确定赝势文件后缀
        pseudo_name = sys.argv[1]
        # 1. SG15
        if pseudo_name == "SG":
            pseudo_suffix = ".SG15.PBE.UPF"
        # 2. PD04
        if pseudo_name == "PD":
            pseudo_suffix = None
        # 3. FHI
        if pseudo_name == "Fh":
            pseudo_suffix = None
        # 4. PWM
        if pseudo_name == "PW":
            pseudo_suffix = None
        # 5. 自定义
        if pseudo_name == "UD":
            pseudo_suffix = None
        
        
        ### Part II. 根据任务类型写入 `etot.input`
        # 1. task_name == SC        
        if self.task_name == "SC":
            in_wg = "F"
            in_rho = "F"
            in_vr = "F"
            out_wg = "T"
            out_rho = "T"
            out_vr = "T"
            out_vatom = "T"
            
            with open(self.etot_path, "a") as f:
                f.write("\n\n")
                f.write("#输入输出设置\n")
                f.write("IN.ATOM = atom.config\n")
                
                ## Note: 赝势部分
                for idx, element in enumerate(["Mo", "S"]):
                    f.write("IN.PSP{0} = {1}{2}\n".format(idx, element, pseudo_suffix))
                
                f.write("IN.WG = {0}\n".format(in_wg))
                f.write("IN.RHO = {0}\n".format(in_rho))
                f.write("IN.VR = {0}\n".format(in_vr))
                f.write("OUT.WG = {0}\n".format(out_wg))
                f.write("OUT.RHO = {0}\n".format(out_rho))
                f.write("OUT.VR = {0}\n".format(out_vr))
                f.write("OUT.VATOM = {0}\n".format(out_vatom))
    
    
    def write_pseudo(self):
        pass