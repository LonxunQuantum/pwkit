import os



def opt1():
    '''
    Description
    -----------
        1. plot_band_structure.x 主要用于画能带图。注意这个程序需要读取:
            - REPORT
            - OUT.FERMI（用于 FERMI Energy 归零）
        2. plot_band_structure.x，之后就会得到
            - bandstructure_1.txt（如果 spin=2，还会输
            出 bandstructure_2.txt）
            - bandstructure.png
            - 如果终端支持转发 X11 端口，还会显示出
            能带图。
    '''
    os.system("plot_band_structure.x")
    
    
if __name__ == "__main__":
    opt1()