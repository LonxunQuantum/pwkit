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


    current_path = os.getcwd()
    rho_xsf_path = os.path.join(current_path, "RHO.xsf")
    if os.path.exists(rho_xsf_path):
        print_sum()


def print_sum():
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入文件:")
    print("\t\tOUT.RHO")
    print("\t* 输出文件:")
    print("\t\tRHO.xsf")
    
    
    print("*{0:-^68}*".format("---------"))

if __name__ == "__main__":
    opt1()