import os 


def opt8():
    '''
    Description
    -----------
        1. convert_from_config.x 主要将 atom.config 转换为 xsf 和 xyz 文件，用于在
            XCRYSDEN（XSF）或者 VMD（XYZ）可视化结构文件；另外也可以将 RELAX，NEB、
            MD，NAMD，TDDFT 计算中产生的 MOVEMENT 转换为 xsf 和 xyz 格式，用于查看结
            构的动态变化。
        2. convert_from_config.x < atom.config，之后就会得到 xatom.xsf、xatom.xyz
    '''
    config_name = input(" 请输入atom.config格式或者MOVEMENT格式的文件名\n------------>>\n")
    os.system("convert_from_config.x < {0}".format(config_name))
    
    
if __name__ == "__main__":
    opt8()