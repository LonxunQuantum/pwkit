import os 


def opt3():
    '''
    Description
    -----------
        1. uspp2upf.x 主要是把 PEtot 需要的 uspp 赝势格式转换为 PWmat 需要的 UPF 格式。
        2. ：uspp2upf.x atom.uspp
    '''
    uspp_name = input(" 请输入uspp格式的文件名\n------------>>\n")
    os.system("echo {0} | uspp2upf.x".format(uspp_name))
    
    
if __name__ == "__main__":
    opt3()