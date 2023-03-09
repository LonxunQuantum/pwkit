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
import re
from etotWriter import EtotWriter
from warning import Warner



'''
Part O. 得到赝势文件夹的路径
'''
# 1. SG15
SG15_DIR_PATH = os.environ.get("SG15_DIR_PATH")

# 2. PD04
PD04_DIR_PATH = os.environ.get("PD04_DIR_PATH")

'''
Part I. Task Type
'''
tasks_str_lst = [
            "SC", "CR", "AR", 
            "NS", "DS", "OS",
            "EP", "MD", "NA",
            "TD", "TC", "TS"
]

def get_upper_task_mark(task_str:str):
    '''
    Descritpion
    -----------
        1. 得到 `task_mark/str` 的大写形式 (`sc` -> `SC`)
    
    Paramaters
    ----------
        1. task_str: str
            - 任务类型的简写
    '''
    return task_str.upper()



'''
Part II. Functional Type
'''
functionals_str_lst = [
        'PE', '91', 'PS',
        'LD', 'H6', 'H3',
        'P0', 'B3', 'TP',
        'SC',
]

def get_upper_functional_mark(functional_str:str):
    '''
    Description
    -----------
        1. 得到 `function_mark/str` 的大写形式
    
    Parameters
    ----------
        1. functional_mark: str
            - 泛函的类型
    '''
    if functional_str == '':
        return "default"
    elif (functional_str.upper() not in functionals_str_lst):
        return "default"
    else:
        return functional_str.upper()
        

'''
Part III. Pseudo Potential Type
'''
pseudos_str_lst = [
            'SG', 'PD', 
            'FH', 'PW',
            'UD',
]

def get_upper_pseudo_mark(pseudo_str:str):
    '''
    Description
    -----------
        1. 得到 `pseudo_mark/str` 的大写形式
    
    Parameters
    ----------
        1. pseudo_mark: str
            - 赝势的类型
    '''    
    if pseudo_str == '':
        return "default"
    elif (pseudo_str.upper() not in pseudos_str_lst):
        return "default"
    else:
        #print(pseudo_str.upper())
        return pseudo_str.upper()


'''
Part IV. Specific Config Type
'''
specifics_str_lst = [
            "SP", "SO", "SN", "CS",
            "PU", "D3", "FF", "SE",
]
def get_upper_specifics_mark(specific_str:str):
    '''
    Description
    -----------
        1. 将剩余的 `self.long_str` 两两分开，并换成大写形式，组成一个列表
    
    Parameters
    ----------  
        1. specific_str: str
            - e.g. `scpespso` -> `spso`
    '''
    ### Note: `specific_str`的长度不可能是奇数，`menu.sh` 之前已经处理过了
    specifics_str_lst = re.findall(".{2}", specific_str)    # 两两分开
    specifics_str_lst = [tmp_str.upper() for tmp_str in specifics_str_lst]
    
    ### Step 2. 如果有 `tmp_str` 不在 `specifics_str_lst` 中，raise ValueError
    ### Note: `specific_str`的长度不可能不存在于 `specifics_str_lst`，`menu.sh` 之前已经处理过了
    #for tmp_str in specifics_str_lst:
    #    if tmp_str not in specifics_str_lst:
    #        raise ValueError
    
    return specifics_str_lst    
    



'''
Part VI. Driver code
'''
class EtotWriterMain(object):
    def __init__(self,
                long_str:str,
                atom_config_path:str,
                sg15_dir_path:str,
                density:float=None,
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
        self.long_str_origin = long_str
        self.atom_config_path = atom_config_path
        self.etot_writer = EtotWriter(
                        atom_config_name=atom_config_path,
                        )
        self.sg15_dir_path = sg15_dir_path
        self.density = density
    
    
    def execute(self):
        '''
        Description
        ----------- 
            1. 
        '''
        self.write_task()
        self.write_functional()
        self.write_accuracy_and_scf()
        self.write_pesudo()
        self.write_specific()
        self.write_other()
        self.write_input_output()

    
    
    def write_task(self):
        '''
        Description
        -----------
            1. 设置`EtotWriter object`的`任务类型`属性
        
        Note
        ----
            1. 在 menu.sh 中，已经提前处理过 `task_mark -> task_name`，因此此处的 `task_mark` 不可能报错
                - 仅调用 `get_upper_task_mark(task_str)` 即可
        '''
        ### Step 1. 得到前两个字符，作为 `task_str`
        p1 = subprocess.Popen(
                        ["echo", "{0}".format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=False,
        )
        p1.wait()
        p2 = subprocess.Popen(
                        ["cut", "-c", "1-2"],
                        stdin=p1.stdout,
                        stdout=subprocess.PIPE,
                        shell=False,
        )
        output, _ = p2.communicate()
        task_str = output.decode().strip()  # 删除末尾的 '\n'
        
        ### Step 2. `etot_writer` 赋予 `任务类型`
        task_str = get_upper_task_mark(task_str=task_str)
        self.etot_writer.write_task(task_name=task_str)
        
        
        ### Step 3. 在 `self.long_str` 删去任务类型
        p1 = subprocess.Popen(
                        ["echo", "{0}".format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=False,
        )
        p1.wait()
        p2 = subprocess.Popen(
                        ["cut", "-c", "3-"],
                        stdin=p1.stdout,
                        stdout=subprocess.PIPE,
                        shell=False,
        )
        output, _ = p2.communicate()
        self.long_str = output.decode().strip()
        
        ### Step 4. 终端输出信息，提醒用户设置完毕
        pp = subprocess.Popen(
                ["echo", " ---> Part I. 任务类型设置成功!"],
                stdout=subprocess.PIPE,
                #stderr=subprocess.PIPE,
                shell=False,                
        )
        output, _ = pp.communicate()
        
        print(output.decode().strip())
   
    
    
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
                    shell=False,
        )
        p1.wait()
        p2 = subprocess.Popen(
                    ['cut', '-c', '1-2'],
                    stdin=p1.stdout,
                    stdout=subprocess.PIPE,
                    shell=False,
        )
        output, _ = p2.communicate()
        functional_str = output.decode().strip()    # 此处的`泛函类型`可能不是真的
        
        ### Step 2. `etot_writer` 赋予 `泛函类型`
        functional_str = get_upper_functional_mark(functional_str=functional_str)
        if functional_str == "default":
            self.etot_writer.write_functional(functional_name="PE")
        else:
            self.etot_writer.write_functional(functional_name=functional_str)
        
            ### Step 3. 删去前两个代表 functional 的字符
            p1 = subprocess.Popen(
                        ['echo', '{0}'.format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=False,
            )
            p1.wait()
            p2 = subprocess.Popen(
                        ['cut', '-c', '3-'],
                        stdin=p1.stdout,
                        stdout=subprocess.PIPE,
                        shell=False,
            )
            output, _ = p2.communicate()
            self.long_str = output.decode().strip()

        ### Step 4. 在 terminal 输出提示信息，提醒用户输出成功
        pp = subprocess.Popen(
                    ['echo', " ---> Part II. 泛函类型设置成功!"],
                    stdout=subprocess.PIPE,
                    shell=False
        )
        output, _ = pp.communicate()
        print(output.decode().strip())
            
        
        
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
        '''
        Description
        -----------
            1. 设置了 `self.pseudo_str_upper` 属性
        '''
        ### Step 1. 取出代表 `赝势类型` 的两个字符
        p1 = subprocess.Popen(
                    ['echo', '{0}'.format(self.long_str)],
                    stdout=subprocess.PIPE,
                    shell=False,
        )
        p1.wait()
        p2 = subprocess.Popen(
                    ['cut', '-c', '1-2'],
                    stdin=p1.stdout,
                    stdout=subprocess.PIPE,
                    shell=False,
        )
        output, _ = p2.communicate()
        pseudo_str = output.decode().strip()  # 此处的`赝势类型`可能不是真的 e.g. `scpesp`
        
        ### Step 2. `etot_writer` 赋予 `赝势类型`
        pseudo_str = get_upper_pseudo_mark(pseudo_str=pseudo_str)
        if pseudo_str == "default":
            self.pseudo_str_upper = "SG"
        else:
            self.pseudo_str_upper = pseudo_str

            ### Step 3. 删去前两个代表 pseudo potential 的字符
            p1 = subprocess.Popen(
                        ['echo', '{0}'.format(self.long_str)],
                        stdout=subprocess.PIPE,
                        shell=False,
            )
            p1.wait()
            p2 = subprocess.Popen(
                        ['cut', '-c', '3-'],
                        stdin=p1.stdout,
                        stdout=subprocess.PIPE,
                        shell=False,
            )
            output, _ = p2.communicate()
            self.long_str = output.decode().strip()
        
        ### Step 4. 
        pp = subprocess.Popen(
                    ['echo', ' ---> Part III. 赝势类型设置成功!'],
                    stdout=subprocess.PIPE,
                    shell=False,
        )
        output, _ = pp.communicate()
        print(output.decode().strip())
    
    
    
    def write_specific(self):
        ### Step 1. 将剩余的字符串(`self.long_str`)中的字母两两分开
        ### e.g. ["SP", "SO", ...]
        specifics_str = get_upper_specifics_mark(self.long_str)
        specifics_str = list( set(specifics_str) )
        ### Step 2. 依次处理 `specifics_str` 中的特殊设置
        for tmp_specific_str in specifics_str:
            if tmp_specific_str == "CS":
                Warner.cs_warning() # 终端输出提示
                charge_density_capacity = float( input(" ------------>>\n").strip() )
                self.etot_writer.write_specific(
                                    specific_str=tmp_specific_str,
                                    charge_density_capacity=charge_density_capacity,
                                    sg15_dir_path=self.sg15_dir_path,
                )
                
            elif tmp_specific_str == "FF":
                Warner.ff_warning() # 终端输出提示
                eletrode_potential = float( input(" ------------>>\n").strip() )
                self.etot_writer.write_specific(
                                    specific_str=tmp_specific_str,
                                    electrode_potential=eletrode_potential,
                )
                                
            else:
                self.etot_writer.write_specific(
                                    specific_str=tmp_specific_str,
                )
        
        ### Step 3. 终端输出信息，提醒用户设置成功
        pp = subprocess.Popen(
                        ['echo', " ---> Part IV. 特殊类型设置成功!"],
                        stdout=subprocess.PIPE,
                        shell=False,
        )
        output, _ = pp.communicate()
        print(output.decode().strip())
    
    
    def write_other(self):
        self.etot_writer.write_other()
        
        
    def write_input_output(self):
        ### Step 1. 找到赝势文件夹
        if self.pseudo_str_upper == "SG":
            pseudo_dir_path = SG15_DIR_PATH
        elif self.pseudo_str_upper == "PD":
            pseudo_dir_path = PD04_DIR_PATH
        
        ### Step 2. 运行
        self.etot_writer.write_input_output(
                        pseudo_name=self.pseudo_str_upper,
                        atom_config_format_file_name=self.atom_config_path,
                        pseudo_dir_path=pseudo_dir_path,
                        )


if __name__ == "__main__": 
    long_str = sys.argv[1]  # 完整的输入 `e.g. scpesgsp`
    current_path = os.getcwd()
    atom_config_path = os.path.join(current_path, sys.argv[2])  # atom.config 的路径
    sg15_dir_path = sys.argv[3]
    
    
    task_str = long_str[:2].upper().strip()
    
    
    try:
        density = float(sys.argv[4])
        etot_writer_main = EtotWriterMain(
                            long_str=long_str,
                            atom_config_path=atom_config_path,
                            sg15_dir_path=sg15_dir_path,
                            density=density
                            
        )
    except IndexError:
        etot_writer_main = EtotWriterMain(
                            long_str=long_str,
                            atom_config_path=atom_config_path,
                            sg15_dir_path=sg15_dir_path,
                            density=None,
        )

    
    
    ### Driver code
    etot_writer_main.execute()