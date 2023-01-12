import os 


def opt6():
    '''
    Description
    -----------
        1. xsf2config.x 主要将 xsf 格式的结构文件转换为 atom.config 文件。
        2. xsf2config.x < atom.xsf，之后就会得到 atom.config
    '''
    xsf_name = input(" 请输入xsf格式的文件名\n------------>>\n")
    os.system("xsf2config.x < {0}".format(xsf_name))
    

if __name__ == "__main__":
    opt6()