import os 
import subprocess
from pflow.io.pwmat.input.gen_vext import GenVext


vr_type2coeffs = {
    '1': ['a4', 'a5', 'a6'],
    '2': ['a4', 'a5', 'a6', 'a7', 'a8', 'a9'],
    '3': ['a4', 'a5']
}

def opt_1():
    '''
    Description
    -----------
        1. 产生 gen.vext 文件，作为 `add_field.x` 的输入
        2. 运行 `add_field.x`，得到 `OUT.REAL.RHO_SP_2.EXT` 文件
        3. 作为etot.input中`IN.VEXT`参数的输入
    
    Note
    ----
        1. 
    '''
    ### Step 1. 得到电场的信息（字符串形式）
    ### Step 1.1. 电场中心
    vr_center_str = input("\n 输入外加电场的中心 (e.g. 0.2,0.6,0.4)\n ------------>>\n")
    try:
        vr_center_lst = [float(coordinate.strip()) for coordinate in vr_center_str.split(',')]
    except ValueError:
        print_error(information="输入电场中心的格式错误!")
        raise SystemExit
    if len(vr_center_lst) != 3:
        print_error(information="输入电场中心的格式错误!")
        raise SystemExit
    #print_error()

    ### Step 2.2. 电场的类型
    print_vr_tips()
    vr_type_str = input(" 输入外加电场的类型 (1 or 2 or 3) \n ------------>>\n")
    vr_type = int(vr_type_str)
    if vr_type not in [1,2,3]:
        print_error(information="输入电场类型的格式错误!")
        raise SystemExit
    
    ### Step 2.3. 电场的参数
    print_vr_tips(int(vr_type_str))
    coeffs_str = input(" 设置电场的参数 ({0}) \n ------------>>\n".format(
                        ','.join(vr_type2coeffs[str(vr_type)]))
    )
    try:
        coeffs_lst = [float(coeff.strip()) for coeff in coeffs_str.split(',')]
    except ValueError:
        print_error(information="输入参数的格式错误!")
        raise SystemExit
    if len(coeffs_lst) != len(vr_type2coeffs[str(vr_type)]):
        print_error(information="输入参数的格式错误!")
        raise SystemExit
    
    
    ### Step 2.4. 是否将电场添加到旧的电势文件上
    add_vr_str = input("\n 是否将新电场加到输入文件势场上 (T or F)\n ------------>>\n")
    if add_vr_str.startswith('T') or add_vr_str.startswith('t'):
        add_vr = True
    elif add_vr_str.startswith('F') or add_vr_str.startswith('f'):
        add_vr = False
    else:
        print_error(information="输入格式错误!")
        raise SystemExit
    
    ### Step 2. 调用pflow生成gen.vext文件
    current_path = os.getcwd()
    gen_vext_path = os.path.join(current_path, "gen.vext")
    gen_vext = GenVext(
                    vr_center_lst,
                    vr_type,
                    add_vr,
                    *coeffs_lst,
                    )
    gen_vext.to(gen_vext_path)
    
    
    ### Step 3. 调用 `add_field.x` 命令
    #p = subprocess.Popen(
    #        ["$PWKIT_ROOT/menu/scripts/add_field.x"],
    #        shell=False
    #)
    #output, _ = p.communicate()
    
    ### 4. print_sum
    #print_sum()
    

def print_vr_tips(vr_type:int=None):
    if vr_type == None:
        print("+{0:-^62}+".format(" 外加电场类型 "))
        print("  * VR_TYPE=1:  Vext(r) = (x-a1)*a4 + (y-a2)*a5 + (z-a3)*a6")
        print('''  * VR_TYPE=2:  Vext(r) = (x-a1)*a4 + (x-a1)^2*a5 + \\
                          (y-a2)*a6 + (y-a2)^2*a7 + \\
                          (z-a3)*a8 + (z-a3)^2*a9''')
        print("  * VR_TYPE=3:  Vext(r) = a4*exp{-[(x-a1)^2+(y-a2)^2+(z-a3)^2]/a5^2}")
        print("+{0:-^68}+".format(""))
    elif vr_type != None:
        print("+{0:-^61}+".format(" 外加电场的参数 "))
        print("\t* a1, a2, a3 为外加电场中心 (分数坐标)")
        if vr_type == 1:
            print("\t* a4, a5, a6, a7, a8 为外加电场的参数")
            print("\t\t- a4, a5, a6 的单位: Hartree/Bohr")
        if vr_type == 2:
            print("\t* a4, a5, a6, a7, a8 为外加电场的参数")
            print("\t\t- a4, a6, a8 的单位: Hartree/Bohr")
            print("\t\t- a5, a7, a9 的单位: Hartree/Bohr^2")
        if vr_type == 3:
            print("\t* a4, a5 为外加电场的参数")
            print("\t\t- a4 的单位: Hartree")
            print("\t\t- a5 的单位: Bohr")
        print("+{0:-^68}+".format(""))


def print_error(information:str):
    '''
    Description
    -----------
        1. 当触发 `dos_decorator` 的错误后，此函数负责输出对应的信息
    '''
    print("\033[0;31m+{0:-^60}+\033[0m".format(" Error "))
    print("\033[0;31m\t* {0}\033[0m".format(information))
    print("\033[0;31m+{0:-^60}+\033[0m".format(""))


def print_sum(vacuum_name:str):
    '''
    Description
    -----------
        1. 输出信息
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入文件:", end='\t')
    print(" - {0}".format("OUT.VR_hion"))
    
    print("\t* 输出文件:", end='\t')
    print(" - {0}".format("RHO.xsf"))
    print(" \t\t\t - {0}".format(vacuum_name))
    print(" \t\t\t - {0}.jpg".format(vacuum_name.split('.')[0]))
    
    
    print("*{0:-^68}*".format("---------"))


if __name__ == "__main__":
    opt_1()