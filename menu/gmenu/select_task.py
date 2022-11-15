#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import sys


# 代表任务类型的字符
tasks_str_lst = [
            "SC", "CR", "AR", 
            "NS", "DS", "OS",
            "EP", "MD", "NA",
            "TD", "TC", "TS"
]


# 防止 Python 程序报错
# 设置默认的任务类型
try: 
    task_str = sys.argv[1]
except IndexError:
    task_str = ""
    

def select_task(task_str:str=task_str):
    '''
    Parameters
    ----------
        1. task_str: str
            长度为2的字符串，用于指定任务类型
    '''
    ### Situation I. 如果输入为q
    if task_str.upper() == "Q":
        print("q")
        return 

    ### Situation II. 如果输入为bb
    if task_str.upper() == "BB":
        print("bb")
        return 
    
    ### Situation III. 当没有输入时，直接返回到 defualt/*)
    if task_str == "":
        print("default")  # 没有对应选项
        return  
    
    ### Situation IV. 解决了大小写的问题：大小写均可以指定 `任务类型`
    if ( task_str.upper() in tasks_str_lst ): 
        print( task_str.upper() )
    else: 
        print("*")  # 没有对应选项

if __name__ == "__main__":
    select_task()