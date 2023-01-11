import os 


def opt7():
    '''
    Description
    -----------
        1. pwscf2config.x 主要将 pwscf 的结构文件转换为 atom.config 文件。
        2. pwscf2config.x 主要将 pwscf 的结构文件转换为 atom.config 文件。
    '''
    pwscf_name = input(" 请输入pwscf格式的文件名\n------------>>\n")
    os.system("pwscf2config.x < {0}".format(pwscf_name))


if __name__ == "__main__":
    opt7()