#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import re
import sys
import copy


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


functional_mark2name = {
                    "PE": "PBE (默认)",
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


pseudo_mark2name = {
                    "SG": "SG15",
                    "PD": "PD04",
                    "FH": "FHI",
                    "PW": "PWM",
                    "UD": "自定义"
}


specific_mark2name = {
    "SP": "自旋极化",
    "SO": "自旋轨道耦合",
    "SN": "非共线磁矩+自旋轨道耦合",
    "CS": "带电体系",
    "PU": "DFT+U",
    "D3": "DFT+D3",
    "FF": "固定电势计算",
    "SE": "溶剂效应",
}



class InputStrPreprocessor(object):
    def __init__(self):
        pass
    
    
    @staticmethod
    def output_content(
                    task_name:str,
                    functional_name:str,
                    pseudo_name:str,
                    specific_name:str,
                    ):
        print("{0:*^80}".format(" 输入设置 "))
        print('''\n\t1. 任务类型: {0}
\t2. 泛函设置: {1}
\t3. 赝势设置: {2}
\t4. 特殊设置: {3}\n'''.format(
                        task_name,
                        functional_name,
                        pseudo_name,
                        specific_name)
        )
        print("{0:*^84}".format(""))
        print()
    
    
    
    @staticmethod
    def output_config(input_str:str,
                    print_mark=True,
                    ):
        '''
        Description
        -----------
            1. 根据输入的 `input_str`，输出：
                - 任务类型
                - 泛函类型
                - 赝势类型
                - 特殊设置
        
        Parameters
        ----------
            1. input_str: str
                e.g. sgpe, ...
        
        Return
        ------
            1. preprocess_mark:
                - 0: 失败
                - 1: 成功
        '''
        if input_str == None:
            InputStrPreprocessor.abort_type_1()
            return
        
        
        splited_strs_lst = re.findall(r'.{2}', input_str)
        
        # 如果输入的字符串长度为奇数，应该把最后一个单个字符加入 `splited_strs_lst`
        if len(input_str) % 2 != 0:
            splited_strs_lst.append(input_str[-1])
        # 令 splited_strs_lst 中的所有字符串(长度为 1/2) 均变为大写
        splited_strs_lst = [splited_str.upper() for splited_str in splited_strs_lst]
            
            
        ### Part I. 任务类型
        try:
            if splited_strs_lst[0] not in task_mark2name.keys():
                InputStrPreprocessor.abort_type_1()
                return 
            else:
                task_mark = splited_strs_lst[0]
                task_name = task_mark2name[task_mark]

                rest_strs_lst = splited_strs_lst[1:]
                #print(task_name) ### 修改
        except IndexError:
            InputStrPreprocessor.abort_type_1()
                
                
        ### Part II. 泛函设置
        try:
            if rest_strs_lst[0] not in functional_mark2name.keys():
                pass
            else:
                functional_mark = rest_strs_lst[0]
                functional_name = functional_mark2name[functional_mark]
                
                rest_strs_lst = rest_strs_lst[1:]
                #print(functional_name) ### 修改
        except IndexError:  # 无泛函设置、赝势设置、特殊设置
            functional_name = "PBE"
            pseudo_name = "SG15"
            specific_name = None
            if print_mark:
                print(1)    # 1 返回给 gmenu 中的 preprocess_mark，用于break输入循环
            return task_name, functional_name, pseudo_name, specific_name

        ### Part III. 赝势设置
        try:
            if rest_strs_lst[0] not in pseudo_mark2name.keys():
                pass
            else:
                pseudo_mark = rest_strs_lst[0]
                pseudo_name = pseudo_mark2name[pseudo_mark]
                
                rest_strs_lst = rest_strs_lst[1:]
                #print(pseudo_name) ### 修改
        except IndexError:  # 无赝势设置、特殊设置
            pseudo_name = "SG15"
            specific_name = None
            if print_mark:
                print(1)    # 1 返回给 gmenu 中的 preprocess_mark，用于break输入循环
            return task_name, functional_name, pseudo_name, specific_name
        
        ### Part IV. 特殊设置
        rest_strs_lst_copy = copy.deepcopy(rest_strs_lst)
        try:
            for _ in range(len(rest_strs_lst_copy)):
                if rest_strs_lst[0] not in specific_mark2name.keys():
                    InputStrPreprocessor.abort_type_2(input_str=input_str)
                    return None
                else:
                    specific_mark = rest_strs_lst[0]
                    specific_name = specific_mark2name[specific_mark]
                    
                    rest_strs_lst = rest_strs_lst[1:]
                    #print(specific_name) ### 修改
        except IndexError:  # 无特殊设置
            specific_name = None
            if print_mark:
                print(1)    # 1 返回给 gmenu 中的 preprocess_mark，用于break输入循环
            return task_name, functional_name, pseudo_name, specific_name
    
    
        
    
        # 全部执行完毕，则返回 1。证明程序执行成功
        print(1)    # 1 返回给 gmenu 中的 preprocess_mark，用于break输入循环
        return 
                
    
    @staticmethod
    def abort_type_1():
        '''
        Description
        -----------
            1. 任务类型错误
        '''
        os.system("echo -e \"\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m\"")
    
    
    @staticmethod
    def abort_type_2(input_str:str):
        '''
        Description
        -----------
            1. 泛函设置错误、赝势设置错误、特殊设置错误
        
        Note
        ----
            1. 由于泛函设置、赝势设置具有默认值，所以难以单独辨别，因此通通到`特殊设置`处处理
        '''
        os.system("echo -e \"\033[35m(*_*) Unsupported selection! Try Again... (*_*)\033[0m\"")
        os.system("echo -e \"\033[35m(*_*) Check your input: {0}! (*_*)\033[0m\"".format(input_str))
        



if __name__ == "__main__":
    try:
        if sys.argv[2] == "output_config_mark":
            case_mark = 2
    except IndexError:
        case_mark = 1
       
    ### Case 1
    if case_mark == 1:
        try:
            input_str = sys.argv[1]
        except:
            input_str = None    
        task_name, functional_name, pseudo_name, specific_name = \
                        InputStrPreprocessor.output_config(
                                                input_str=input_str,
                                                print_mark=True,
                                                )

    ### Case 2
    if case_mark == 2:
        try:
            input_str = sys.argv[1]
        except:
            input_str = None    
        task_name, functional_name, pseudo_name, specific_name = \
                        InputStrPreprocessor.output_config(
                                                input_str=input_str,
                                                print_mark=False,
                                                )
        
        InputStrPreprocessor.output_content(
                                        task_name=task_name,
                                        functional_name=functional_name,
                                        pseudo_name=pseudo_name,
                                        specific_name=specific_name
                                        )