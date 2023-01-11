import os


def opt1():
    '''
    Description
    -----------
        1. convert_rho.x 主要是把 PWmat 输出的二进制文件 OUT.RHO、OUT.VR 转换为 VESTA、
XcrySDen 可读的格式。
        2. 使用方法：convert_rho.x OUT.RHO，之后就会得到 RHO.xsf
    
    '''
    os.system("convert_rho.x OUT.RHO")


if __name__ == "__main__":
    opt1()