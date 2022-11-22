#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import re
import sys


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




def output_config(input_str):
    '''
    Return
    ------
        1. Return 分为 3 种类型：
            1. "abort_task"
            2. "abort_input";`input_str`
            3. "output_config";自洽计算;PBE;...
        2. Note: 所有返回的字符串，各个部分用 ";" 分离
            
    Note
    ----
        1. `print(result)`: 会把 result 返回给 shell 脚本
        2. `return result`: 不会把 result 返回给 shell 脚本 
    '''
    # 如果输入的字符串长度为奇数，应该把最后一个单个字符加入 `splited_strs_lst`
    if len(input_str) % 2 != 0:
        # Abort: Check your input!
        print( ";".join(["abort_input", input_str]) )
        return
    splited_strs_lst = re.findall(r'.{2}', input_str)
    splited_strs_lst = [splited_str.upper() for splited_str in splited_strs_lst]
    
    
    ### Part I. 任务类型
    task_mark = splited_strs_lst[0]
    if ( task_mark not in task_mark2name.keys() ):
        # Abort: 任务类型
        print("abort_task")
        return
    task_name = task_mark2name[task_mark]
    splited_strs_lst.pop(0)
    rest_strs_lst = splited_strs_lst
    
    if len(rest_strs_lst) == 0:
        functional_name = "PBE"
        pseudo_name = "SG15"
        specific_name = "*!*"
        # print
        print(";".join([task_name, functional_name, pseudo_name, specific_name]))
        return    
    
    
    ### Part II. 泛函设置
    functional_mark = rest_strs_lst[0]
    if ( functional_mark in functional_mark2name.keys() ):
        functional_name = functional_mark2name[functional_mark]
        rest_strs_lst.pop(0)
    else:   # 默认泛函：PBE
        functional_name = "PBE"

    if len(rest_strs_lst) == 0:
        pseudo_name = "SG15"
        specific_name = "*!*"
        print(";".join([task_name, functional_name, pseudo_name, specific_name]))
        return    
        
        
    ### Part III. 赝势设置
    pseudo_mark = rest_strs_lst[0]
    if ( pseudo_mark in pseudo_mark2name.keys() ):
        pseudo_name = pseudo_mark2name[pseudo_mark]
        rest_strs_lst.pop(0)
    else:   # 默认赝势：SG15
        pseudo_name = "SG15"

    if len(rest_strs_lst) == 0:
        specific_name = "*!*"
        print(";".join([task_name, functional_name, pseudo_name, specific_name]))
        return        
        
    ### Part IV. 特殊设置
    specific_names_lst = []
    specific_length = len(rest_strs_lst)


    for _ in range(specific_length):
        specific_mark = rest_strs_lst[0]
        
        if specific_mark not in specific_mark2name.keys():
            ### Abort: Check your input
            print( ";".join(["abort_input", input_str]) )
            return 
        specific_name = specific_mark2name[specific_mark]
        specific_names_lst.append(specific_name)
        rest_strs_lst.pop(0)
    
    # 删除重复的specific_name
    specific_names_lst = list(set(specific_names_lst))
    
    # return    
    print(";".join([task_name, functional_name, pseudo_name] + specific_names_lst))
    return    


if __name__ == "__main__":
    try:
        output_config(input_str=sys.argv[1])
    except:
        # Abort: 任务类型 -- 对应于无输入的时候
        print("abort_task")