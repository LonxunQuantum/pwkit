import os


def optb():
    '''
    Description
    -----------
        1. atominfo.x 主要是给出 PWmat 的结构文件 atom.config 的几何信息.
        2. atominfo.x atom.config，屏幕输出
    '''
    config_name = input(" 请输入atom.config格式的文件名\n------------>>\n")
    os.system("atominfo.x {0}".format(config_name))


if __name__ == "__main__":
    optb()