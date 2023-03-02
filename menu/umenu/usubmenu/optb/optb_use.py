import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List


def opt_b():
    '''
    Description
    -----------
        1. 使用PWMat进行SCF/RELAX计算（计算一个在z方向上有真空的体系），得到 OUT.VR
        2. 使用 `convert_rho.x OUT.VR` 得到 `RHO.xsf`
        3. 再使用 `vacuum.x`，得到
            - vacuum_x.dat
            - vacuum_y.dat
            - vacuum_z.dat`
        4. 功函数 = 真空能级 - 费米能级
    
    Note
    ----
        1. 1 Ha = 27.2 eV
        2. 区分：
            - `OUT.VR`: 包含交换关联势
            - `OUT.VR_hion`: 不包含交换关联势
            - 绘制真空能级时，最好使用 `OUT.VR_hion`
        3. 区分：
            1. `convert_rho.x`: 无论输入什么名字的文件，输入 RHO.xsf
            2. `convert_rho_new.x`: 输入 OUT.VR; 输出 OUT.VR.xsf
    '''
    ### Step 1. convert_rho.x OUT.VR(可以是其他名字)
    current_path = os.getcwd()
    out_vr_name = "OUT.VR_hion"
    while  ( not os.path.exists(
            os.path.join(current_path, out_vr_name))
            ):
        os.system('''        echo -e "\n\033[31m - 未搜索到名为 {0} 的文件，需要手动指定OUT.RHO格式的文件名...\033[0m\n"'''.format(out_vr_name))
        out_vr_name = input(" OUT.RHO格式的文件名\n------------>>\n")
    os.system("$PWKIT_ROOT/menu/scripts/convert_rho.x {0} > /dev/null".format(out_vr_name))
    
    ### Step 2. 输入真空方向, 运行 `vacuum.x`
    direction = input(" 输入真空的方向 (e.g. z)\n------------>>\n")
    vacuum_name = "vacuum_{0}.dat".format(direction)
    os.system("$PWKIT_ROOT/menu/scripts/vacuum_new.x > /dev/null")
    
    
    ### Step 3. 读取 vacuum_x/y/z.dat
    df_vacuum = pd.read_csv(
                    os.path.join(current_path, vacuum_name),
                    sep='\s+',
                    )
    xs_lst = list( df_vacuum.iloc[:, 0].to_numpy() )
    ys_lst = list( df_vacuum.iloc[:, 1].to_numpy() )
    
    print(
        ys_lst.index( np.max(ys_lst) )
        )
    
    ### Step 4. 绘制图像
    output_png_path = os.path.join(current_path, "{0}.jpg".format(vacuum_name.split('.')[0]))
    plot_vacuum(
            xs_lst=xs_lst,
            potential_lst=ys_lst, 
            direction=direction,
            output_png_path=output_png_path,
            )
    
    ### Step 5. print sum
    print_sum(
            vacuum_name=vacuum_name,
            )
    
    

def plot_vacuum(
            xs_lst:List[float],
            potential_lst:List[float],
            direction:str,
            output_png_path:str,
            ):
    '''
    Description
    -----------
        1. 绘制 "Energy - length along axis"
    '''
    plt.figure(figsize=(10, 8))
    ### Step 0.1. 全局设置
    #plt.rcParams["font.family"] = "Times New Roman"
    #plt.rcParams['mathtext.fontset'] = 'custom'
    #plt.rcParams['mathtext.rm'] = 'Times New Roman'
    #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
    #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
    ### Step 0.2. 刻度线朝内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    plt.plot(xs_lst, potential_lst, c="lightslategray", lw=3)
    
    # 1. xlabel / ylabel
    plt.xlabel("Length along {0}-axis".format(direction),
               fontsize=24,
               fontweight="bold")
    plt.ylabel("Energy (eV)",
               fontsize=24,
               fontweight="bold")
    # 2. xticks / yticks
    ax = plt.gca()
    #ax.axes.xaxis.set_visible(False)
    plt.xticks(fontsize=20, 
        fontweight="bold"
        )
    plt.yticks(fontsize=20, 
        fontweight="bold"
        )
    # 3. 刻度线的粗细
    plt.tick_params(
        width=2,        # 刻度线的粗细
        length=5,       # 刻度线的长短
        #labelsize=28   # 刻度线的字体大小
        )
    # 4. 设置坐标轴的粗细
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(1.5);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(1.5);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(1.5);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(1.5);###设置右边坐标轴的粗细
    # 5. xrange / yrange
    plt.xlim(0, max(xs_lst))

    plt.savefig(
            output_png_path,
            dpi=300,
            bbox_inches="tight",
            )


def get_vacuum_level(
                xs_lst:List[float], 
                potentials_lst:List[float],
                threshold:float=0.01
                ):
    for idx in range(2, len(xs_lst)):
        xs_array = np.array(xs_lst)
        potentials_array = np.array(potentials_lst)
        slope, intercept = np.polyfit(xs_array, potentials_array, 1)
    

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
    opt_b()