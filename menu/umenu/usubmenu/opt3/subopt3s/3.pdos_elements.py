import os
import pandas as pd
import numpy as np
from pflow.io.pwmat.output.dostotalspin import Dostotalspin
from pflow.io.pwmat.output.outfermi import OutFermi
import matplotlib.pyplot as plt

from exception_decorator import dos_decorator


'''
Parr I. no_ispin
'''
def max_and_min_noispin(df:pd.DataFrame):
    max_energy = df.loc[:, "Energy"].max()
    min_energy = df.loc[:, "Energy"].min()
    return max_energy, min_energy


@dos_decorator
def main_noispin(dos_totalspin_projected_name):
    ### Step 1. 运行 `plot_DOS_interp.x`，得到 `DOS.totalspin_projected`
    current_path = os.getcwd()
    dos_totalspin_projected_path = os.path.join(
                                        current_path,
                                        dos_totalspin_projected_name)
    os.system('plot_DOS_interp.x > /dev/null')
    
    
    ### Step 2. 用 `DOS.totalspin_projected` 初始化 `Dostotalspin` 对象
    dos_totalspin_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_totalspin_projected_path,
                                )
    df_elements = dos_totalspin_projected_object.get_pdos_elements()
    
    ### Step 2.1. 若存在 OUT.FERMI，则减去费米能级
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = out_fermi_object.get_efermi()
        df_elements.loc[:, "Energy"] = df_elements.loc[:, "Energy"] - efermi_ev
    
    
    ### Step 3. 获取绘制的能量范围
    ### Step 3.1. 得到能量范围 - [e_min_value, e_max_value]
    e_max_value, e_min_value = max_and_min_noispin(df_elements)
    e_max_value = np.round(e_max_value, 4)
    e_min_value = np.round(e_min_value, 4)

    ### Step 3.2. 输入能量范围
    print(" 能量范围是 {0} eV ~ {1} eV。输入绘制的能量范围 (e.g. -2,2)".format(e_min_value, e_max_value))
    e_range_str = input(" ------------>>\n")
    e_max = float( e_range_str.split(',')[1].strip() )
    e_min = float( e_range_str.split(',')[0].strip() )
    if (e_max > e_max_value) or (e_min < e_min_value):
        # 超出所能绘制的能量范围
        raise KeyError("\n\033[0;31m Error: 超出能量范围! \033[0m")
        #print('\n\033[0;31m Error: 超出能量范围! \033[0m')
        #raise SystemExit

    ### 3.3. 根据输入的能量范围筛选数据 -- `df_elements_plot`
    mask = (df_elements.loc[:, "Energy"] < e_max) & \
            (df_elements.loc[:, "Energy"] > e_min)
    df_elements_plot = df_elements.loc[mask, :]
    
    ### 4 绘制图像
    plot_pdos_elements_noispin(
                df_pdos_elements=df_elements_plot,
                E_min=e_min,
                E_max=e_max,
                efermi_ev=efermi_ev,
                )
    
    ### 5. 输出总结
    print_sum_noispin(efermi_ev=efermi_ev)



def plot_pdos_elements_noispin(
                df_pdos_elements:pd.DataFrame,
                E_min:float,
                E_max:float,
                efermi_ev:float,
                ):
    colors_lst = plt.cm.tab20(np.linspace(0, 1, 20))
    current_path = os.getcwd()

    ### Step 1. Plot PDOS
    ### Step 1.1. 全局设置
    #plt.rcParams["font.family"] = "Times New Roman"
    #plt.rcParams['mathtext.fontset'] = 'custom'
    #plt.rcParams['mathtext.rm'] = 'Times New Roman'
    #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
    #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
    ### Step 1.2. 刻度线朝内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    ### Step 1.3. Plot PDOS
    plt.figure(figsize=(10, 8))
    for idx, tmp_column in enumerate(df_pdos_elements.columns.to_list()):
        if tmp_column == "Energy":
            continue
        plt.plot(
                df_pdos_elements.loc[:, "Energy"],
                df_pdos_elements.loc[:, tmp_column],                
                c=colors_lst[idx],
                lw="2",
                label=tmp_column,
                )
    # 1. xlabel / ylabel
    plt.xlabel("Energy (eV)",
               fontsize=24,
               fontweight="bold")
    plt.ylabel("Density of State",
               fontsize=24,
               fontweight="bold")
    # 2. xticks / yticks
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
    # 5. xrange
    #delta = float(0.05 * (max-min))
    #min = min - delta
    #max = max + delta/dos
    plt.xlim(E_min, E_max)
    plt.ylim(bottom=0)
    
    legend_font = {
                    "size" : 18, 
                    "weight": "bold"
                    }
    plt.legend(prop=legend_font,
                frameon=False)

    # 6. 保存图片
    if efermi_ev:
        output_jpg_path = os.path.join(current_path, "dos_elements_ShiftFermi.jpg")
        output_csv_path = os.path.join(current_path, "dos_elements_ShiftFermi.csv")
        df_pdos_elements.to_csv(
                        output_csv_path,
                        sep=",",
                        index=False)
    else:
        output_jpg_path = os.path.join(current_path, "dos_elements.jpg")
        output_csv_path = os.path.join(current_path, "dos_elements.csv")
        df_pdos_elements.to_csv(
                        output_csv_path,
                        sep=",",
                        index=False)
    plt.savefig(
            output_jpg_path,
            dpi=300,
            bbox_inches="tight",
            )
    

def print_sum_noispin(efermi_ev:float):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输出文件:", end="")
    if efermi_ev:
        print("\t - {0}".format("dos_elements_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_elements_ShiftFermi.jpg"))
    else:
        print("\t - {0}".format("dos_elements.csv"))
        print("\t\t\t - {0}".format("dos_elements.jpg"))
    if not efermi_ev:
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[0;31m \t* 当前目录下没有 OUT.FERMI 文件，态密度没有减去费米能级!\033[0m\n", end="")

    print("*{0:-^68}*".format("---------"))





'''
Parr II. ispin
'''
def max_and_min_ispin(
                df_up:pd.DataFrame,
                df_down:pd.DataFrame,
                ):
    max_energy_up = df_up.loc[:, "Energy"].max()
    min_energy_up = df_up.loc[:, "Energy"].min()
    
    max_energy_down = df_down.loc[:, "Energy"].max()
    min_energy_down = df_down.loc[:, "Energy"].min()
    
    max_energy = max([max_energy_up, max_energy_down])
    min_energy = min([min_energy_up, min_energy_down])
    return max_energy, min_energy


@dos_decorator
def main_ispin(
            dos_spinup_projected_name:str,
            dos_spindown_projected_name:str,
            ):
    '''
    Parameters
    ----------
        1. dos_spinup_projected_name: str
            - 
        2. dos_spindown_projected_name: str
            - 
    '''
    ### Step 1. 运行 `plot_DOS_interp.x`，得到 `DOS.totalspin_projected`
    current_path = os.getcwd()
    dos_spinup_projected_path = os.path.join(
                                    current_path,
                                    dos_spinup_projected_name)
    dos_spindown_projected_path = os.path.join(
                                    current_path,
                                    dos_spindown_projected_name)
    os.system('plot_DOS_interp.x > /dev/null')
    
    
    ### Step 2. 用 `DOS.totalspin_projected` 初始化 `Dostotalspin` 对象
    dos_spinup_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_spinup_projected_path,
                                )
    dos_spindown_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_spindown_projected_path,
                                )
    df_elements_spinup = dos_spinup_projected_object.get_pdos_elements()
    df_elements_spindown = dos_spindown_projected_object.get_pdos_elements()
    
    ### Step 2.1. 若存在 OUT.FERMI，则减去费米能级
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = out_fermi_object.get_efermi()
        df_elements_spinup.loc[:, "Energy"] = df_elements_spinup.loc[:, "Energy"] - efermi_ev
        df_elements_spindown.loc[:, "Energy"] = df_elements_spindown.loc[:, "Energy"] - efermi_ev
    
    
    ### Step 3. 获取绘制的能量范围
    ### Step 3.1. 得到能量范围 - [e_min_value, e_max_value]
    e_max_value, e_min_value = max_and_min_ispin(
                                    df_up=df_elements_spinup,
                                    df_down=df_elements_spindown,
                                )
    e_max_value = np.round(e_max_value, 4)
    e_min_value = np.round(e_min_value, 4)

    ### Step 3.2. 输入能量范围
    print(" 能量范围是 {0} eV ~ {1} eV。输入绘制的能量范围 (e.g. -2,2)".format(e_min_value, e_max_value))
    e_range_str = input(" ------------>>\n")
    e_max = float( e_range_str.split(',')[1].strip() )
    e_min = float( e_range_str.split(',')[0].strip() )
    if (e_max > e_max_value) or (e_min < e_min_value):
        #print('\n\033[0;31m Error: 超出能量范围! \033[0m')
        raise KeyError("超出能量范围")

    ### 3.3. 根据输入的能量范围筛选数据 -- `df_elements_plot`
    mask_spinup = (df_elements_spinup.loc[:, "Energy"] < e_max) & \
                (df_elements_spinup.loc[:, "Energy"] > e_min)
    df_elements_spinup_plot = df_elements_spinup.loc[mask_spinup, :]
    mask_spindown = (df_elements_spindown.loc[:, "Energy"] < e_max) & \
                (df_elements_spindown.loc[:, "Energy"] > e_min)
    df_elements_spindown_plot = df_elements_spindown.loc[mask_spindown, :]
    
    ### 4 绘制图像
    plot_pdos_elements_ispin(
                df_pdos_elements_spinup=df_elements_spinup_plot,
                df_pdos_elements_spindown=df_elements_spindown_plot,
                E_min=e_min,
                E_max=e_max,
                efermi_ev=efermi_ev,
                )
    
    ### 5. 输出总结
    print_sum_ispin(efermi_ev=efermi_ev)


def plot_pdos_elements_ispin(
                df_pdos_elements_spinup:pd.DataFrame,
                df_pdos_elements_spindown:pd.DataFrame,
                E_min:float,
                E_max:float,
                efermi_ev:float,
                ):
    colors_lst = plt.cm.tab20(np.linspace(0, 1, 20))
    current_path = os.getcwd()

    ### Step 1. Plot PDOS
    ### Step 1.1. 全局设置
    #plt.rcParams["font.family"] = "Times New Roman"
    #plt.rcParams['mathtext.fontset'] = 'custom'
    #plt.rcParams['mathtext.rm'] = 'Times New Roman'
    #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
    #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
    ### Step 1.2. 刻度线朝内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    ### Step 1.3. Plot PDOS
    plt.figure(figsize=(10, 8))
    plt.axhline(y=0, lw=1.5, c="black")
    for tmp_spin, tmp_df_pdos_elements in zip(
                                            ["up", "down"],
                                            [df_pdos_elements_spinup, df_pdos_elements_spindown]
                                        ):
        for idx, tmp_column in enumerate(tmp_df_pdos_elements.columns.to_list()):
            if tmp_column == "Energy":
                continue
            if tmp_spin == "down":
                color_idx = df_pdos_elements_spinup.shape[1] - 1 + idx
            else:
                color_idx = idx
            plt.plot(
                    tmp_df_pdos_elements.loc[:, "Energy"],
                    tmp_df_pdos_elements.loc[:, tmp_column],
                    c=colors_lst[color_idx],
                    lw="2",
                    label="{0}_{1}".format(tmp_column, tmp_spin),
                    )
    # 1. xlabel / ylabel
    plt.xlabel("Energy (eV)",
               fontsize=24,
               fontweight="bold")
    plt.ylabel("Density of State",
               fontsize=24,
               fontweight="bold")
    # 2. xticks / yticks
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
    # 5. xrange
    #delta = float(0.05 * (max-min))
    #min = min - delta
    #max = max + delta/dos
    plt.xlim(E_min, E_max)
    #plt.ylim(bottom=0)
    
    legend_font = {
                    "size" : 18, 
                    "weight": "bold"
                    }
    plt.legend(prop=legend_font,
                frameon=False)

    # 6. 保存图片
    if efermi_ev:
        output_jpg_path = os.path.join(current_path, "dos_elements_ShiftFermi.jpg")
        output_csv_spinup_path = os.path.join(current_path, "dos_spinup_elements_ShiftFermi.csv")
        output_csv_spindown_path = os.path.join(current_path, "dos_spindown_elements_ShiftFermi.csv")
        
        df_pdos_elements_spinup.to_csv(
                        output_csv_spinup_path,
                        sep=",",
                        index=False)
        df_pdos_elements_spindown.to_csv(
                        output_csv_spindown_path,
                        sep=",",
                        index=False)
    else:
        output_jpg_path = os.path.join(current_path, "dos_elements.jpg")
        output_csv_spinup_path = os.path.join(current_path, "dos_spinup_elements.csv")
        output_csv_spindown_path = os.path.join(current_path, "dos_spindown_elements.csv")
        
        df_pdos_elements_spinup.to_csv(
                        output_csv_spinup_path,
                        sep=",",
                        index=False)
        df_pdos_elements_spindown.to_csv(
                        output_csv_spindown_path,
                        sep=",",
                        index=False)
        
    plt.savefig(
            output_jpg_path,
            dpi=300,
            bbox_inches="tight",
            )


def print_sum_ispin(efermi_ev:float):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输出文件:", end="")
    if efermi_ev:
        print("\t - {0}".format("dos_spinup_elements_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_spindown_elements_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_elements_ShiftFermi.jpg"))
    else:
        print("\t - {0}".format("dos_spinup_elements.csv"))
        print("\t\t\t - {0}".format("dos_spindown_elements.csv"))
        print("\t\t\t - {0}".format("dos_elements.jpg"))
    if not efermi_ev:
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[0;31m \t* 当前目录下没有 OUT.FERMI 文件，态密度没有减去费米能级!\033[0m\n", end="")

    print("*{0:-^68}*".format("---------"))



'''
Part III. Driver code
'''
if __name__ == "__main__":
    current_path = os.getcwd()
    
    ### Step 1. 如果没有 DOS.input 直接报错
    dos_input_path = os.path.join(current_path, "DOS.input")
    if not os.path.exists(dos_input_path):
        print('\n\033[0;31m   * Error: 请先使用PWkit生成 DOS.input 文件! \033[0m')
        raise SystemExit
    
    
    ### Step 2. 绘制能带图
    dos_totalspin_projected_name = "DOS.totalspin_projected"
    dos_spinup_projected_name = "DOS.spinup_projected"
    dos_spindown_projected_name = "DOS.spindown_projected"
    
    dos_spinup_path = os.path.join(current_path, "DOS.spinup")
    dos_spindown_path = os.path.join(current_path, "DOS.spindown")
    
    # mark_spin: True--打开自旋，False--关闭自旋
    mark_ispin = os.path.exists(dos_spinup_path) and os.path.exists(dos_spindown_path)
    if mark_ispin:
        main_ispin(
            dos_spinup_projected_name=dos_spinup_projected_name,
            dos_spindown_projected_name=dos_spindown_projected_name,
            )
    else:
        main_noispin(dos_totalspin_projected_name=dos_totalspin_projected_name)