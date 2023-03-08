'''
Description
-----------
    1. This file is for `gsubmenu1.menu`
'''
import os
import re
import subprocess
import shutil
import linecache
from pflow.io.publicLayer.structure import DStructure


# 1. 任务的mark: 任务名
task_mark2name = {
                    "SC": "自洽计算",
                    "CR": "晶格+原子位置优化",
                    "AR": "固定晶格优化原子位置",
                    
                    "NS": "非自洽计算",
                    "DS": "原子轨道投影（态密度）",
                    "OS": "振子强度计算",
                    
                    "EP": "电子声子耦合系数计算",
                    "MD": "从头算分子动力学",
                    "NA": "非绝热分子动力学",
                    
                    "TD": "含时密度泛函计算",
                    "TC": "过渡态计算",
                    "TS": "过渡态搜索",
}

# 2. 泛函的mark: 泛函名
functional_mark2name = {
                    "PE": "PBE",
                    "91": "PW91",
                    "PS": "PBEsol",
                    "LD": "CA-PZ",
                    "H6": "HSE06",
                    
                    "H3": "HSE03",
                    "P0": "PBE0",
                    "B3": "B3LYP",
                    "TP": "TPSS",
                    "SC": "SCAN",
}

# 3. 赝势的mark: 赝势名
pseudo_mark2name = {
                    "SG": "SG15",
                    "PD": "PD04",
                    "FH": "FHI",
                    "PW": "PWM",
                    "UD": "自定义"
}

# 4. 特殊设置的mark: 特殊设置名
specific_mark2name = {
    "SP": "自旋极化",
    "SO": "自旋轨道耦合",
    "SN": "非共线磁矩+自旋轨道耦合",
    "CS": "带电体系",
    "PU": "DFT+U",
    "D3": "DFT-D3",
    "FF": "固定电势计算",
    "SE": "溶剂效应",
}


# 5. file_mark2format
file_mark2format = {
        1: "pwmat",
        2: "vasp",
        3: "mcsqs",
        4: "json",
        5: "xsf",
        6: "yaml",
        7: "cssr",
        8: "prismatic",
}



def fname_exists(fname:str):
    '''
    Description
    -----------
        1. 判断名为 fname 的文件是否存在
        2. absolute_path = os.path.join(current_path, fname)
        
    Parameters
    ----------
        1. fname: str
            - 文件名
    
    Return
    ------
        1. mark_exist: bool
        - 文件是否存在
    '''
    current_path = os.getcwd()
    file_path = os.path.join(current_path, fname)
    
    mark_exist = None
    if os.path.exists(file_path):
        mark_exist = True
    else:
        mark_exist = False
    
    return mark_exist



class InformationReminder(object):
    '''
    Description
    -----------
        1. PWkit 在运行过程中的各种提示
    
    
    '''
    def __init__(self, remider_type:str):
        self.remider_type = remider_type
        
        
    def reminder(self):
        if self.remider_type == "file_mark2format":
            InformationReminder.reminder_file_mark2format()
        
        if self.remider_type == "":
            pass
    
    @staticmethod
    def reminder_file_mark2format():
        print("+{0:-^58}+".format(" Warm Tips "))
        print("\t* 结构文件的格式:")
        print("\t\t1.pwmat  2.vasp  3.mcsqs  4.json")
        print("\t\t5.xsf    6.yaml  7.cssr   8.prismatic")
        print("+{0:-^58}+".format("---------"))
        




class InformationAbortor(object):
    '''
    Description
    -----------
        1. 面对各种输入出错时，报错的提示信息 
    '''
    def __init__(self, error_type:str):
        '''
        Parameters
        ----------
            1. error_type: str
                1) 
                2) 
                3)
        '''
        self.error_type = error_type

    
    @staticmethod    
    def abort_input(input_from_terminal:str):
        '''
        Description
        -----------
            1. For `get_config_for_etot()`
                1. terminal 中输入的前两个字符不在 `task_mark2name` 字典中
        '''
        print("\033[35m(*_*) Unsupported selection! Try Again... (*_*)\033[0m")
        print( "\033[35m(*_*) Check your input: {0}! (*_*)\033[0m".format(input_from_terminal))
    
    
    @staticmethod
    def abort_task():
        '''
        Description
        -----------
            1. For `get_config_for_etot()`
                1. terminal 中输入的字符长度为奇数
                2. terminal 中输入的 `functional_mark`, `pseudo_mark`, `specific_mark` 不在对应的字典中
        '''
        print("\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m")



def get_config_for_etot(
                input_from_terminal:str,
                ):
    '''
    Description
    -----------
        1. input_from_terminal: str
            - 用户从 terminal 输入的字符串
    
    Return 
    ------
        1. 
            - Right: "自洽计算;PBE;SG15;*!*"
            - Right: "自洽计算;PBE;SG15;自旋极化;DFT+U"
            - Wrong: "abort_input;scsp1" -- 输入长度为奇数的字符串
            - Wrong: "abort_task" -- 输入的任务类型不在 `task_mark2name` 中
    '''
    ### Step 1. 如果输入的字符串长度为奇数，提醒用户检查输入
    if (len(input_from_terminal) % 2 != 0):
        return ";".join(["abort_input", input_from_terminal])
    strs_lst = re.findall(r'.{2}', input_from_terminal) # 将字符串每两个字符分开
    strs_lst = [tmp_str.upper() for tmp_str in strs_lst]    # 全部变成大写，好处理
    
    ### Step 2. 根据 `strs_lst` 设置 `etot.input` 的设置
    ### Step 2.1. 任务类型
    task_mark = strs_lst[0]
    if ( task_mark not in task_mark2name.keys() ):
        return "abort_task"
    task_name = task_mark2name[task_mark]
    strs_lst.pop(0) # 处理完任务类型后，将 `task_mark` 从 `strs_lst` 中移除
    
    if len(strs_lst) == 0:
        functional_name = "PBE"
        pseudo_name = "SG15"
        specific_name = "*!*"
        return ";".format(
                    [task_name, functional_name, pseudo_name, specific_name]
                    )
    
    ### Step 2.2. 泛函类型
    functional_mark = strs_lst[0]
    if ( functional_mark in functional_mark2name.keys() ):
        functional_name = functional_mark2name[functional_mark]
        strs_lst.pop()  # 处理完泛函类型后，将 `functional_mark` 从 `strs_lst` 中移除
    else:
        functional_name = "PBE"
    
    if len(strs_lst) == 0:
        pseudo_name = "SG15"
        specific_name = "*!*"
        return ";".join([task_name, functional_name, pseudo_name, specific_name])
    
    ### Step 2.3. 赝势设置
    pseudo_mark = strs_lst[0]
    if ( pseudo_mark in pseudo_mark2name.keys() ):
        pseudo_name = pseudo_mark2name[pseudo_mark]
        strs_lst.pop(0)
    else:
        pseudo_name = "SG15"
        
    if len(strs_lst) == 0:
        specific_name = "*!*"
        return ";".join([task_name, functional_name, pseudo_name, specific_name])
    
    ### Step 2.4. 特殊设置
    specific_names_lst = []
    specific_length = len(strs_lst)
    
    for _ in range(specific_length):    # 依次处理 `特殊设置的mark`
        specific_mark = strs_lst[0]
        
        if specific_mark not in specific_mark2name.keys():
            ### Abort: Check your input
            return ";".join(["abort_input", input_from_terminal])
        
        specific_names_lst.append( specific_mark2name[specific_mark] )
        strs_lst.pop(0) # 处理完这个 `specific_mark`, 将其从 `strs_lst` 中移除
    
    # 删除重复的 specific_name
    specific_names_lst = list(set(specific_names_lst))
    
    # return
    return ";".join([task_name, functional_name, pseudo_name] + specific_names_lst)


def output_config_for_etot(
                str_splitted:str,
                ):
    '''
    Description
    -----------
        1. 在 terminal 输出 `etot.input` 的信息。
        ************************************* 任务设置 *************************************
                1. 任务类型: 自洽计算
                2. 泛函设置: PBE
                3. 赝势设置: SG15
                4. 特殊设置: 无
        ************************************************************************************
    
    Parameters
    ----------
        1. str_splitted: str
            - `str_splitted` 来自于本文件的 `get_config_for_etot` 的输出
    '''
    # e.g. config_names_lst = [ "自洽计算", "PBE", "SG15", "*!*"]
    config_names_lst = str_splitted.split(';')
    
    ### Step 1. 各种设置的确定
    ### Step 1.1. 任务类型
    task_name = config_names_lst[0]
    
    ### Step 1.2. 泛函设置
    functional_name = config_names_lst[1]
    
    ### Step 1.3. 赝势设置
    pseudo_name = config_names_lst[2]
    
    ### Step 1.4. 特殊设置
    specific_names = config_names_lst[3:]
    
    
    ### Step 2. 输出各种设置
    print("{0:*80}".format(" 任务设置 "))
    print("\t1. 任务类型: {0}".format(task_name))
    print("\t2. 泛函设置: {1}".format(functional_name))
    print("\t3. 赝势设置: {2}".format(pseudo_name))
    if specific_names == "None":
        print("\t4. 特殊设置: {0}".format("无"))
    else:
        print("\t4. 特殊设置: {0}".format("、".join(specific_names)))
    print("{0:*^84}\n".format(""))
    


def search_atom_comfig_format_file():
    '''
    Description
    -----------
        1. 寻找 `atom.config` 格式的文件
    
    Return
    ------  
        1. tmp_file_name: str
            - atom.config 格式的文件名
    '''
    current_path = os.getcwd()
    
    ### Step 1. 有 `atom.config` 就直接返回 `atom.config`
    if os.path.exists( os.path.join(current_path, "atom.config") ):
        return "atom.config"
    
    ### Step 2. 没有 `atom.config` 再检查其他文件，是否是 `atom.config` 格式
    for tmp_file_name in os.listdir(current_path):        
        tmp_file_path = os.path.join(current_path, "tmp_file_path")
        
        ### Step 2.1. 不用检查如下这些文件
        if ( not os.path.isfile(tmp_file_path) ) or \
                    ( "UPF" in tmp_file_name ) or \
                    ( "IN" in tmp_file_name ) or \
                    ( "OUT" in tmp_file_name) or \
                    ( "slurm" in tmp_file_name) or \
                    ( "output" in tmp_file_name ) or \
                    ( "REPORT" in tmp_file_name ) or \
                    ( "etot.input" in tmp_file_name ):
            continue
        
        ### Step 2.2. 判断剩下的文件是否有 `atom.config` 格式的文件
        ### Step 2.2.1. 将第2行和第6行的所有字符串变成大写形式
        # tmp_rows_lst_upper_2: ['Lattice', 'vector']
        # tmp_rows_lst_upper_6: ['Position,', 'move_x,', 'move_y,', 'move_z']
        tmp_rows_lst_upper_2 = [
                        tmp_str.strip().upper() \
                        for tmp_str in linecache.getline(tmp_file_path, 2).split()
        ]
        tmp_rows_lst_upper_6 = [
                        tmp_str.strip().upper() \
                        for tmp_str in linecache.getline(tmp_file_path, 6).split()
        ]
        # tmp_rows_lst_upper_2: ['LATTICE', 'VECTOR']
        # tmp_rows_lst_upper_6: ['POSITION,', 'MOVE_X,', 'MOVE_Y,', 'MOVE_Z']
        if ("LATTICE" in tmp_rows_lst_upper_2 and \
            "POSITION" in tmp_rows_lst_upper_6
            ):
            return tmp_file_name
        
    return None
        
    
    
def get_atom_config_format_name():
    '''
    Description
    -----------
        1. 得到 PWMat 格式的文件名
        2. 如果当前文件夹下不存在 atom.config 格式的文件，则自行输入并转化结构成 atom.config 格式
    
    Return
    ------
        1. atom_config_format_file_name: str
            1. 如果存在atom.config格式的文件，直接返回`该文件名`
            2. 如果不存在 `atom.config`，（转换格式后，生成`atom.config`）,返回`atom.config`
    '''
    ### Step 1. 得到当前文件夹下，文件的数目
    process1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    process2 = subprocess.Popen(["wc", "-l"], stdout=subprocess.PIPE)
    output, error = process2.communicate()
    num_files = int(output)
    
    ### Step 2. 除非得到 atom.config 格式的文件，否则一直在 `while` 循环内
    current_path = os.getcwd()
    atom_config_format_file_name = None
    atom_config_format_name = None

    ### Case 1. 当前文件夹下，有格式为 `atom.config` 的文件
    atom_config_format_file_name = search_atom_comfig_format_file()
    if atom_config_format_file_name != None:
        print(" - 搜索到 PWmat 格式的结构文件: {0}".format(atom_config_format_file_name))
        return atom_config_format_file_name
    
    ### Case 2. 当前文件夹下，不存在名为 `atom.config` 的文件
    else:
        print("\033[31m - 未搜索到 PWmat 格式的结构文件，需要手动指定结构文件的格式和文件名...\033[0m")
        while (True):    
            # 提示:
            #   1.pwmat  2.vasp  3.mcsqs  4.json
            #   5.xsf    6.yaml  7.cssr   8.prismatic
            InformationReminder.reminder_file_mark2format()
            file_format_mark = input(" 结构文件的格式\n--------------->>\n")
            if file_format_mark in file_mark2format.keys():
                break
            print("\033[35m(*_*) 输入的文件格式错误 (*_*)\033[0m")
        while (True):  
            file_name = input(" 结构文件的名字\n--------------->>\n")
            if os.path.exists( os.path.join(current_path, file_name) ):
                break
            print("\033[35m(*_*) 输入的文件名不存在... (*_*)\033[0m")
    
        atom_config_format_name = file_mark2format[file_format_mark]
        atom_config_format_file_name = file_name
        
        ### Step 3. 若 Case==2，将输入的文转换为 atom.config
        structure = DStructure.from_file(
                        file_path=os.path.join(current_path, atom_config_format_file_name),
                        file_format=atom_config_format_name,
                        )
        structure.to(filename=os.path.join(current_path, "atom.config"))
        
        atom_config_format_file_name = "atom.config"
        
        return atom_config_format_file_name


