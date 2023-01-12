import os 


def opt9():
    '''
    Description
    -----------
        1. config2poscar.x主要是把PWmat的结构文件atom.config转换为POSCAR格式。
        2. config2poscar.x atom.config，之后就会得到 POSCAR.pwmat
    '''
    config_name = input(" 请输入POSCAR格式的文件名\n------------>>\n")
    os.system("config2poscar.x {0}".format(config_name))


if __name__ == "__main__":
    opt9()