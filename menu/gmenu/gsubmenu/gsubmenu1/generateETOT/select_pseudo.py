import sys


# 代表赝势设置的字符
pseudos_str_lst = [
            "SG", "PD", 
            "FH", "PW",
            "UD"
]


# 防止 Python 程序报错
try: 
    pseudo_str = sys.argv[1]
except IndexError:
    pseudo_str = ""   # 跳转到 default)
    

def select_task(pseudo_str:str=pseudo_str):
    '''
    Parameters
    ----------
        1. pseudo_str: str
            长度为2的字符串，用于泛函设置
    '''
    ### Situation I. 如果输入为q
    if pseudo_str.upper() == "Q":
        print("q")
        return 

    ### Situation II. 如果输入为bb
    if pseudo_str.upper() == "BB":
        print("bb")
        return 
    
    ### Situation III. 当没有输入时，直接返回到 defualt/*)
    if pseudo_str == "":
        print("default")  # 没有对应选项
        return  
    
    ### Situation IV. 解决了大小写的问题：大小写均可以指定 `赝势设置`
    if ( pseudo_str.upper() in pseudos_str_lst ): 
        print( pseudo_str.upper() )
    else: 
        print("default")  # 没有对应选项,认为这一项没有输入

if __name__ == "__main__":
    select_task()