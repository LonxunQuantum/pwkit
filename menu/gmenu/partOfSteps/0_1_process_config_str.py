#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import sys


def process_str(config_str:str):
    '''
    Description
    -----------
        1. 处理包含 ; 的字符串, e.g. "自洽计算;PBE;SG15;*!*"
    
    Parameters
    ----------
        1. config_str: str
            - e.g. "自洽计算;PBE;SG15;*!*"
    '''
    # e.g. configs_lst = [ "自洽计算", "PBE", "SG15", "*!*"]
    configs_lst = config_str.split(";")
    
    ### Part I. 各种设置的确定
    # 1. 任务类型
    task_name = configs_lst[0]
    
    # 2. 泛函设置
    functional_name = configs_lst[1]
    
    # 3. 赝势设置
    pseudo_name = configs_lst[2]
    
    # 4. 特殊设置
    specific_names = configs_lst[3:]
    if specific_names[0] == "*!*":
        specific_names = "None"
        
    ### Part II. 输出各种设置
    print("{0:*^80}".format(" 任务设置 "))
    print("\t1. 任务类型: {0}".format(task_name))
    print("\t2. 泛函设置: {0}".format(functional_name))
    print("\t3. 赝势设置: {0}".format(pseudo_name))
    if specific_names == "None":
        print("\t4. 特殊设置: {0}".format("无"))
    else:
        print("\t4. 特殊设置: {0}".format("、".join(specific_names)))
    print("{0:*^84}\n".format(""))
    
    
if __name__ == "__main__":
    process_str(sys.argv[1])