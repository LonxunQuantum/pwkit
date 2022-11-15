#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import sys


# 代表任务类型的字符
tasks_str_lst = [
            "SC", "CR", "AR", 
            "NS", "DS", "OS",
            "EP", "MD", "NA",
            "TD", "TC", "TS"
]


task_str = sys.argv[1]

def select_task(task_str:str=task_str):
    '''
    Parameters
    ----------
        1. task_str: str
            长度为2的字符串，用于指定任务类型
    '''
    # 解决了大小写的问题：大小写均可以指定 `任务类型`
    if ( task_str.upper() in tasks_str_lst ): 
        return task_str.upper()


if __name__ == "__main__":
    print(select_task())