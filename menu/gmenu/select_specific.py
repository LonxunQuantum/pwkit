#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import sys


# 代表特殊设置的字符
functionals_str_lst = [
            "SP", "SO", "SN", "CS",
            "PU", "D3", "FF", "SE",
]


# 防止 Python 程序报错
try: 
    functional_str = sys.argv[1]
except IndexError:
    functional_str = ""   # 跳转到 default)
    

def select_task(functional_str:str=functional_str):
    '''
    Parameters
    ----------
        1. functional_str: str
            长度为2的字符串，用于泛函设置
    '''
    ### Situation I. 如果输入为q
    if functional_str.upper() == "Q":
        print("q")
        return 

    ### Situation II. 如果输入为bb
    if functional_str.upper() == "BB":
        print("bb")
        return 
    
    ### Situation III. 当没有输入时，直接返回到 defualt/*)
    if functional_str == "":
        print("default")  # 没有对应选项
        return  
    
    ### Situation IV. 解决了大小写的问题：大小写均可以指定 `特殊设置`
    if ( functional_str.upper() in functionals_str_lst ): 
        print( functional_str.upper() )
    else: 
        print("*")  # 没有对应选项,认为这一项没有输入

if __name__ == "__main__":
    select_task()