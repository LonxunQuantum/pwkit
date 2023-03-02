import os
from pflow.io.pwmat.input.dos_input import DosInput



def choose_mark_method():
    '''
    Description
    -----------
        1. Gaussian Broading / Interpolation
    '''
    print("{0:-^50}".format(" 插值选择 "))
    print(" 1) Gaussian Broading    2) Interpolation\n")
    mark_method = input(" ------------>>\n")
    return mark_method


def input_ismear():
    print(" 高斯展宽的数值 (默认: 0.04)")
    ismear = input(" ------------>>\n")
    try:
        _ = float(ismear)
    except ValueError:
        ismear = 0.04
    return ismear 


def input_num_energies():
    print(" 能量点的数目 (默认: 4000)")
    num_energies = input(" ------------>>\n")
    try:
        _ = float(num_energies)
    except ValueError:
        num_energies = 4000
    return num_energies
        

def input_grid_interp():
    print(" K点插值网格 (默认: 6,6,6)")
    grid_interp = input(" ------------>>\n")
    try:
        grids_interp_lst = grid_interp.split(',')
    except ValueError:
        grids_interp_lst = ["6", "6", "6"]
        
    if len(grids_interp_lst) != 3:
        grids_interp_lst = ["6", "6", "6"]
    
    grids_interp_lst = [int(value) for value in grids_interp_lst]
    return grids_interp_lst


def main():
    '''
    Description
    -----------
        1. 生成 DOS.input 文件
    '''
    mark_method = choose_mark_method()
    ismear = input_ismear()
    num_energies = input_num_energies()
    grids_interp_lst = input_grid_interp()
    
    dos_input_object = DosInput(
                        mark_atoms=0,
                        mark_method=mark_method, 
                        ismear=float(ismear), 
                        num_energies=int(num_energies),
                        grid_interp=grids_interp_lst,
                        )
    
    current_path = os.getcwd()
    output_path = os.path.join(current_path, "DOS.input")
    dos_input_object.to(output_path=output_path)

    print_sum()



def print_sum():
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输出文件:", end="")
    print("\t - {0}".format("DOS.input"))
        
    print("*{0:-^68}*".format("---------"))
    
    

if __name__ == "__main__":
    main()