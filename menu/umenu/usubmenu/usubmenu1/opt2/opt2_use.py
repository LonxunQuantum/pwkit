import os



def opt4():
    '''
    Description
    -----------
        1. poscar2config.x 主要将 POSCAR 格式的结构文件转换为 atom.config 文件。
        2. poscar2config.x < POSCAR，之后就会得到 atom.config
    '''
    #poscar_name = os.system("read -p '  ------------>> ' opt")
    poscar_name = input(" 请输入POSCAR格式的文件名\n------------>>\n")
    os.system("poscar2config.x < {0}".format(poscar_name))
    
    
if __name__ == "__main__":
    opt4()