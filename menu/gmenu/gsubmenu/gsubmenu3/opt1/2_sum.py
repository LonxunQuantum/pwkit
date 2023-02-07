import sys


def print_sum_opt1(atom_config_path:str):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 结构文件:", end="")
    print("\t - {0}".format(atom_config_path))
    print("\t* 输出文件:", end="")
    print("\t - {0}".format("HIGHK"))
    print("\t\t\t - {0}".format("gen.kpt"))
    print("\t\t\t - {0}".format("HIGH_SYMMETRY_POINT"))
    print("\t\t\t - {0}".format("IN.KPT"))
    
    
    print("*{0:-^68}*".format("---------"))


if __name__ == "__main__":
    print_sum_opt1(sys.argv[1])