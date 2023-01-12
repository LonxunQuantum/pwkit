import os 


def opt5():
    '''
    Description
    -----------
        1. 将CASTEP的cell格式的结构文件转换为atom.config文件。
        2. cell2config.x < atom.cell，之后就会得到 atom.config
    '''
    cell_name = input(" 请输入cell格式的文件名\n------------>>\n")
    os.system("cell2config.x < {0}".format(cell_name))
    

if __name__ == "__main__":
    opt5()