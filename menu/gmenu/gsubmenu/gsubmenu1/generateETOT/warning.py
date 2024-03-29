import sys


class Warner(object):
    @staticmethod
    def kmesh_warning():
        '''
        Description
        -----------
            1. 选择 KMesh for `MP_N123` in etot.input
        '''
        print("+{0:-^68}+".format(" Warm Tips "))
        print("\t* Accuracy Levels: Gamma-Only: 0;")
        print("\t                   Low:        0.06~0.04;")
        print("\t                   Medium:     0.04~0.03")
        print("\t                   Fine:       0.02~0.01")
        print("\t* 0.03~0.04 is Generally Precise Enough!")
        print("+{0:-^68}+".format("---------"))
        
    
    @staticmethod
    def cs_warning():
        print("+{0:-^68}+".format(" Warm Tips "))
        print("\t* 输入带电量 (|绝对值|≤8.000，可以保留3位小数)")
        print("\t* 电子数 = 中性电子数(通过赝势计算所得) - 带电量")
        print("+{0:-^68}+".format("---------"))
        

    @staticmethod
    def ff_warning():
        print("+{0:-^68}+".format(" Warm Tips "))
        print("\t* 提示输入电极电势(单位伏特V，|绝对值|≤5.000，保留2位小数)")
        print("\t* Ef=-4.42-电极电势值 ")
        print("\t* 额外需要输出文件IN.SOLVENT (自动生成)")
        print("+{0:-^68}+".format("---------"))
        
    
    @staticmethod
    def se_warning():
        print("+{0:-^68}+".format(" Warm Tips "))
        print("\t* 额外需要输出文件IN.SOLVENT (自动生成)")
        print("+{0:-^68}+".format("---------"))


if __name__ == "__main__":
    if sys.argv[1] == "kmesh_warning":
        Warner.kmesh_warning()
    
    if sys.argv[1] == "CS":
        Warner.cs_warning()
        
    if sys.argv[1] == "FF":
        Warner.ff_warning()
        
    if sys.argv[1] == "SE":
        Warner.se_warning()