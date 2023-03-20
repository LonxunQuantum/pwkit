import re
import os 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from typing import List, Union
from pflow.io.pwmat.output.fatabandstructureTxt import FatbandStructure
from pflow.io.pwmat.output.outfermi import OutFermi
from pflow.io.pwmat.input.inkpt import Inkpt
from band_decorator import (
                EnergyRangeError, 
                EnergyRangeFormatError,
                ElementNotExistsError,
                band_decorator
)



def get_hsp(
        in_kpt_path:str,
        atom_config_path:str
):
    '''
    Description
    -----------
        1. 得到对称点的`名称`和`距gamma的距离（unit: 埃）
    
    Return
    ------
        1. hsp_names_lst: List[str]
            - 高对称点的名字
        2. hsp_xs_lst: List[float]
            - 高对称点的横坐标（在 bandstructure 上）
    '''
    in_kpt_object = Inkpt(in_kpt_path=in_kpt_path)
    ### Step 1. `idx2hsp`: e.g. 
    idx2hsp = in_kpt_object._get_idx2hsp()
    ### Step 2. `distances_from_gamma`: e.g. 
    distances_from_gamma = \
                in_kpt_object.get_distance_from_gamma_A(
                            atom_config_path=atom_config_path
                            )
    ### Step 3. 分别得到对称点的`名称`和`距gamma的距离（unit: 埃）`
    hsp_names_lst = [value for key, value in idx2hsp.items()]
    hsp_idxs_lst = [key for key, value in idx2hsp.items()]
    hsp_xs_lst = [distances_from_gamma[tmp_idx] for tmp_idx in hsp_idxs_lst]
    
    return hsp_names_lst, hsp_xs_lst
    

@band_decorator
def main_nospin():
    ### Step 0. 运行 `plot_fatband_structure.x` 生成 `fatbandstructure_1.txt`
    '''
    Note
    ----
        1. 注意 plot_fatbandstructure.x 可以自己处理 OUT.FERMI，不需要我们再次处理！！！
    '''
    ### Step 1. 文件路径
    current_path = os.getcwd()
    fatbandstructure_txt_path = os.path.join(current_path, "fatbandstructure_1.txt")
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    in_kpt_path = os.path.join(current_path, "IN.KPT")
    atom_config_path = os.path.join(current_path, "atom.config")
    
    ### Step 2. 若当前目录下存在 OUT.FERMI，则所有本征能量需要减去费米能级
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = out_fermi_object.get_efermi()
    
    ### Step 3. xs_lst, 能带结构的横坐标是 `当前kpoint距前一个kpoint之间的距离`
    fatbandstructure = FatbandStructure(fatbandstructure_txt_path=fatbandstructure_txt_path)
    element_dfs_lst:List[pd.DataFrame] = fatbandstructure.get_element_dfs_lst()
    xs_lst = list( element_dfs_lst[0].loc[:, "KPOINT"] )
    

    ### Step 4. yss_scatter_lst, scatter 纵坐标为某元素对应的权重
    input_element_string = input("\n 输入投影到的元素\n ------------>>\n")
    element_for_fatband = input_element_string.strip()
    yss_scatter_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    for tmp_element_df in element_dfs_lst:
        yss_scatter_lst.append( 
                tmp_element_df.filter(
                        regex=re.compile("^{0}".format(element_for_fatband), re.IGNORECASE), 
                        axis=1
                ).values.flatten().tolist()
        )    
    for tmp_lst in yss_scatter_lst:
        if tmp_lst == []:
            raise ElementNotExistsError("体系中不存在 {0} 元素!".format(element_for_fatband))
    ### Step 5. yss_line_lst，能带结构的纵坐标是 `band#1, kpoint#1 对应的本征能量    
    ### Step 5.1. 输入需要绘制的能量区间 (e_min ~ e_max)
    df_raw = fatbandstructure._preprocess()
    e_min_value = df_raw.loc[:, "ENERGY"].min()
    e_max_value = df_raw.loc[:, "ENERGY"].max()
    input_energy_string = input(
        "\n 能量范围是 {0} eV ~ {1} eV。请输入绘制的能量范围 (e.g. -5,5)\n ------------>>\n".format(
        round(e_min_value, 3),
        round(e_max_value, 3),
        ))
    e_min = float( input_energy_string.split(',')[0].strip() )
    e_max = float( input_energy_string.split(',')[1].strip() )
    if ( (e_min < e_min_value) or (e_max > e_max_value) ):
        raise EnergyRangeError("输入的能量区间过大!")
    
    ### Step 5.2. 得到能带的纵坐标 (减去？不减去？费米能级) -- `plot_fatbandstructure.x` 已经处理过了
    yss_line_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    #if (efermi_ev):
    #    for tmp_element_df in element_dfs_lst:
    #        tmp_element_df.loc[:, "ENERGY"] = tmp_element_df.loc[:, "ENERGY"] - efermi_ev
    #        yss_line_lst.append( list(tmp_element_df.loc[:, "ENERGY"]) )
    #else:
    for tmp_element_df in element_dfs_lst:
        tmp_element_df.loc[:, "ENERGY"] = tmp_element_df.loc[:, "ENERGY"]
        yss_line_lst.append( list(tmp_element_df.loc[:, "ENERGY"]) )        
    
    ### Step 6. 得到高对称点的横坐标和名称
    hsp_names_lst, hsp_xs_lst = get_hsp(
                                    in_kpt_path=in_kpt_path,
                                    atom_config_path=atom_config_path,
                                    )
     
    ### Step 7. 绘制 fatbandstructure
    #plot_fatband_nospin()
    plot_fatband_nospin(xs_lst=xs_lst,
                        yss_line_lst=yss_line_lst,
                        yss_scatter_lst=yss_scatter_lst,
                        element=element_for_fatband,
                        x_min=0,
                        x_max=df_raw.loc[:, "KPOINT"].max(),
                        e_min=e_min,
                        e_max=e_max,
                        hsp_names_lst=hsp_names_lst,
                        hsp_xs_lst=hsp_xs_lst,
                        efermi_ev=efermi_ev
                        )

    ### Step 8. 输出
    print_sum_nospin(
            efermi_ev=efermi_ev,
            element=element_for_fatband
    )


def plot_fatband_nospin(
                xs_lst:List[float],
                yss_line_lst:List[List[float]],
                yss_scatter_lst:List[List[float]],
                element:str,
                x_min:float,
                x_max:float,
                e_min:float,
                e_max:float,
                hsp_names_lst:List[str],
                hsp_xs_lst:List[float],
                efermi_ev:Union[float, bool]
                ):
    COLOR_LINE = "steelblue"
    COLOR_SCATTER = "orangered"
    plt.figure(figsize=(10, 8))
    for idx_band in range(len(yss_line_lst)):
        plt.plot(xs_lst, yss_line_lst[idx_band],
                c=COLOR_LINE,
                lw=2,
                zorder=1
                )
        mark_sizes = [size*80 for size in yss_scatter_lst[idx_band]]
        plt.scatter(xs_lst, yss_line_lst[idx_band],
                    s=mark_sizes,
                    c=COLOR_SCATTER,
                    zorder=2)

    # 1. xlabel / ylabel
    plt.ylabel("Energy (eV)",
               fontsize=24,
               fontweight="bold")
    # 2. xticks / yticks
    ax = plt.gca()
    #ax.axes.xaxis.set_visible(False)
    #plt.xticks(fontsize=20, 
    #    fontweight="bold"
    #    )
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
    
    
    # 5. 高对称点
    ax.set_xticks(hsp_xs_lst)
    ax.set_xticklabels(hsp_names_lst)
    plt.xticks(fontsize=20, 
        fontweight="bold"
        )
    #ax.tick_params(axis='x', labelsize=20, weight="bold")
    
    # 6. 高对称点处的虚线
    for x_value in hsp_xs_lst:
        plt.axvline(
                x=x_value,
                lw=2, 
                linestyle="--",
                color="black",
                zorder=0
                )

    # 7. xrange / yrange
    plt.xlim(x_min, x_max)
    plt.ylim(e_min, e_max)
    
    # 8. legend
    line1 = Line2D([0], [0], color=COLOR_SCATTER, 
                   linewidth=0,
                   marker='o', markersize=10)
    legend_font = {"size" : 18, 
                    "weight": "bold"
                    }
    legend_handles = [line1]
    legend_labels = [element.capitalize()]
    ax.legend(legend_handles, legend_labels, 
            prop=legend_font,
            frameon=False)    

    # 9. Save
    if efermi_ev:
        png_name = "./fatbandstructure_{0}_ShiftFermi.png".format(element)
    else:
        png_name = "./fatbandstructure_{0}.png".format(element)

    plt.savefig(png_name,
                dpi=300,
                bbox_inches="tight"
    )



def print_sum_nospin(efermi_ev:Union[float, bool], element:str): 
    print("*{0:-^68}*".format( " Summary "))
    
    print("\t* 输入文件:", end='\t')
    print(" - {0}".format("final.config"))
    print(" \t\t\t - {0}".format("IN.KPT"))
    if (efermi_ev != False):
        print(" \t\t\t - {0}".format("OUT.FERMI"))
    
    print("\t* 输出文件:", end='\t')
    print(" - {0}".format("fatbandstructure_1.txt"))
    if (efermi_ev == False):
        print(" \t\t\t - {0}".format("fatbandstructure_{0}.png".format(element)))
    else:
        print(" \t\t\t - {0}".format("fatbandstructure_{0}_ShiftFermi.png".format(element)))

    # Warning: 
    if (efermi_ev == False):
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[1;31m \t* 当前目录下没有 OUT.FERMI 文件，能带没有减去费米能级!\033[0m\n", end="")
    
    print("*{0:-^68}*".format("---------"))




'''
Part II. spin
'''
@band_decorator
def main_spin():
    '''
    Note
    ----
        1. 注意 plot_fatbandstructure.x 可以自己处理 OUT.FERMI，不需要我们再次处理！！！
    '''
    
    ### Step 1. 文件路径
    current_path = os.getcwd()
    fatbandstructure_txt_1_path = os.path.join(current_path, "fatbandstructure_1.txt")
    fatbandstructure_txt_2_path = os.path.join(current_path, "fatbandstructure_2.txt")
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    in_kpt_path = os.path.join(current_path, "IN.KPT")
    atom_config_path = os.path.join(current_path, "atom.config")
    
    ### Step 2. 若当前目录下存在 OUT.FERMI，则所有本征能量需要减去费米能级
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = out_fermi_object.get_efermi()
    
    ### Step 3. xs_lst, 能带结构的横坐标是 `当前kpoint距前一个kpoint之间的距离`
    fatbandstructure_1 = FatbandStructure(fatbandstructure_txt_path=fatbandstructure_txt_1_path)
    fatbandstructure_2 = FatbandStructure(fatbandstructure_txt_path=fatbandstructure_txt_2_path)
    element_dfs_1_lst:List[pd.DataFrame] = fatbandstructure_1.get_element_dfs_lst()
    element_dfs_2_lst:List[pd.DataFrame] = fatbandstructure_2.get_element_dfs_lst()
    xs_lst = list( element_dfs_1_lst[0].loc[:, "KPOINT"] )

    ### Step 4. yss_scatter_lst, scatter 纵坐标为某元素对应的权重
    input_element_string = input("\n 输入投影到的元素\n ------------>>\n")
    element_for_fatband = input_element_string.strip()
    yss_scatter_1_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    yss_scatter_2_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    for tmp_element_df in element_dfs_1_lst:
        yss_scatter_1_lst.append( 
                tmp_element_df.filter(
                        regex=re.compile("^{0}".format(element_for_fatband), re.IGNORECASE), 
                        axis=1
                ).values.flatten().tolist()
        )
        
    for tmp_lst in yss_scatter_1_lst:
        if tmp_lst == []:
            raise ElementNotExistsError("体系中不存在 {0} 元素!".format(element_for_fatband))
        
    for tmp_element_df in element_dfs_2_lst:
        yss_scatter_2_lst.append( 
                tmp_element_df.filter(
                        regex=re.compile("^{0}".format(element_for_fatband), re.IGNORECASE), 
                        axis=1
                ).values.flatten().tolist()
        )
    
    ### Step 5. yss_line_lst，能带结构的纵坐标是 `band#1, kpoint#1 对应的本征能量    
    ### Step 5.1. 输入需要绘制的能量区间 (e_min ~ e_max)
    df_raw_1 = fatbandstructure_1._preprocess()
    df_raw_2 = fatbandstructure_2._preprocess()
    e_min_value_1 = df_raw_1.loc[:, "ENERGY"].min()
    e_max_value_1 = df_raw_1.loc[:, "ENERGY"].max()
    e_min_value_2 = df_raw_2.loc[:, "ENERGY"].min()
    e_max_value_2 = df_raw_2.loc[:, "ENERGY"].max()
    e_min_value = min([e_min_value_1, e_min_value_2])
    e_max_value = min([e_max_value_1, e_max_value_2])
    input_energy_string = input(
        "\n 能量范围是 {0} eV ~ {1} eV。请输入绘制的能量范围 (e.g. -5,5)\n ------------>>\n".format(
        round(e_min_value, 3),
        round(e_max_value, 3),
        ))
    e_min = float( input_energy_string.split(',')[0].strip() )
    e_max = float( input_energy_string.split(',')[1].strip() )
    if ( (e_min < e_min_value) or (e_max > e_max_value) ):
        raise EnergyRangeError("输入的能量区间过大!")
    
    ### Step 5.2. 得到能带的纵坐标 (减去？不减去？费米能级) -- `plot_fatbandstructure.x` 已经处理过了
    yss_line_1_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    yss_line_2_lst:List[List[float]] = []   # 每条能带上各个kpoints的本征能量
    #if (efermi_ev):
    #    for tmp_element_df in element_dfs_lst:
    #        tmp_element_df.loc[:, "ENERGY"] = tmp_element_df.loc[:, "ENERGY"] - efermi_ev
    #        yss_line_lst.append( list(tmp_element_df.loc[:, "ENERGY"]) )
    #else:
    for tmp_element_df in element_dfs_1_lst:
        tmp_element_df.loc[:, "ENERGY"] = tmp_element_df.loc[:, "ENERGY"]
        yss_line_1_lst.append( list(tmp_element_df.loc[:, "ENERGY"]) )        
    for tmp_element_df in element_dfs_2_lst:
        tmp_element_df.loc[:, "ENERGY"] = tmp_element_df.loc[:, "ENERGY"]
        yss_line_2_lst.append( list(tmp_element_df.loc[:, "ENERGY"]) )  
    
    ### Step 6. 得到高对称点的横坐标和名称
    hsp_names_lst, hsp_xs_lst = get_hsp(
                                    in_kpt_path=in_kpt_path,
                                    atom_config_path=atom_config_path,
                                    )
     
    ### Step 7. 绘制 fatbandstructure
    #plot_fatband_nospin()
    plot_fatband_spin(xs_lst=xs_lst,
                        yss_line_1_lst=yss_line_1_lst,
                        yss_line_2_lst=yss_line_2_lst,
                        yss_scatter_1_lst=yss_scatter_1_lst,
                        yss_scatter_2_lst=yss_scatter_2_lst,
                        element=element_for_fatband,
                        x_min=0,
                        x_max=df_raw_1.loc[:, "KPOINT"].max(),
                        e_min=e_min,
                        e_max=e_max,
                        hsp_names_lst=hsp_names_lst,
                        hsp_xs_lst=hsp_xs_lst,
                        efermi_ev=efermi_ev
                        )

    ### Step 8. 输出
    print_sum_spin(
            efermi_ev=efermi_ev,
            element=element_for_fatband
    )


def plot_fatband_spin(
                xs_lst:List[float],
                yss_line_1_lst:List[List[float]],
                yss_line_2_lst:List[List[float]],
                yss_scatter_1_lst:List[List[float]],
                yss_scatter_2_lst:List[List[float]],
                element:str,
                x_min:float,
                x_max:float,
                e_min:float,
                e_max:float,
                hsp_names_lst:List[str],
                hsp_xs_lst:List[float],
                efermi_ev:Union[float, bool]
                ):
    COLORS_LINE = ["steelblue", "greenyellow"]
    COLORS_SCATTER = ["orangered", "blueviolet"]
    plt.figure(figsize=(10, 8))
    for idx_band in range(len(yss_line_1_lst)):
        plt.plot(xs_lst, yss_line_1_lst[idx_band],
                c=COLORS_LINE[0],
                lw=2,
                alpha=0.5,
                zorder=1,
                )
        mark_sizes = [size*80 for size in yss_scatter_1_lst[idx_band]]
        plt.scatter(xs_lst, yss_line_1_lst[idx_band],
                    s=mark_sizes,
                    c=COLORS_SCATTER[0],
                    zorder=2)
    for idx_band in range(len(yss_line_2_lst)):
        plt.plot(xs_lst, yss_line_2_lst[idx_band],
                c=COLORS_LINE[1],
                lw=2,
                alpha=0.5,
                zorder=1
                )
        mark_sizes = [size*80 for size in yss_scatter_2_lst[idx_band]]
        plt.scatter(xs_lst, yss_line_2_lst[idx_band],
                    s=mark_sizes,
                    c=COLORS_SCATTER[1],
                    zorder=2)

    # 1. xlabel / ylabel
    plt.ylabel("Energy (eV)",
               fontsize=24,
               fontweight="bold")
    # 2. xticks / yticks
    ax = plt.gca()
    #ax.axes.xaxis.set_visible(False)
    #plt.xticks(fontsize=20, 
    #    fontweight="bold"
    #    )
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
    
    
    # 5. 高对称点
    ax.set_xticks(hsp_xs_lst)
    ax.set_xticklabels(hsp_names_lst)
    plt.xticks(fontsize=20, 
        fontweight="bold"
        )
    #ax.tick_params(axis='x', labelsize=20, weight="bold")
    
    # 6. 高对称点处的虚线
    for x_value in hsp_xs_lst:
        plt.axvline(
                x=x_value,
                lw=2, 
                linestyle="--",
                color="black",
                zorder=0
                )

    # 7. xrange / yrange
    plt.xlim(x_min, x_max)
    plt.ylim(e_min, e_max)
    
    # 8. legend
    line1 = Line2D([0], [0], color=COLORS_SCATTER[0], 
                   linewidth=0,
                   marker='o', markersize=10)
    line2 = Line2D([0], [0], color=COLORS_SCATTER[1], 
                   linewidth=0,
                   marker='o', markersize=10)
    legend_font = {"size" : 18, 
                    "weight": "bold"
                    }
    legend_handles = [line1, line2]
    legend_labels = [
                    "{0}_up".format(element.capitalize()),
                    "{0}_down".format(element.capitalize()),
    ]
    ax.legend(legend_handles, legend_labels, 
            prop=legend_font,
            frameon=False)    

    # 9. Save
    if efermi_ev:
        png_name = "./fatbandstructure_{0}_ShiftFermi.png".format(element)
    else:
        png_name = "./fatbandstructure_{0}.png".format(element)

    plt.savefig(png_name,
                dpi=300,
                bbox_inches="tight"
    )


def print_sum_spin(efermi_ev:Union[float, bool], element:str): 
    print("*{0:-^68}*".format( " Summary "))
    
    print("\t* 输入文件:", end='\t')
    print(" - {0}".format("final.config"))
    print(" \t\t\t - {0}".format("IN.KPT"))
    if (efermi_ev != False):
        print(" \t\t\t - {0}".format("OUT.FERMI"))
    
    print("\t* 输出文件:", end='\t')
    print(" - {0}".format("fatbandstructure_1.txt"))
    print(" \t\t\t - {0}".format("fatbandstructure_2.txt"))
    if (efermi_ev == False):
        print(" \t\t\t - {0}".format("fatbandstructure_{0}.png".format(element)))
    else:
        print(" \t\t\t - {0}".format("fatbandstructure_{0}_ShiftFermi.png".format(element)))

    # Warning: 
    if (efermi_ev == False):
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[1;31m \t* 当前目录下没有 OUT.FERMI 文件，能带没有减去费米能级!\033[0m\n", end="")
    
    print("*{0:-^68}*".format("---------"))




if __name__ == "__main__":
    os.system("$PWKIT_ROOT/menu/scripts/plot_fatband_structure.x > /dev/null")
    current_path = os.getcwd()
    fatbandstructure_txt_2_path = os.path.join(current_path, "fatbandstructure_2.txt")
    
    if os.path.exists(fatbandstructure_txt_2_path):
        main_spin()
    else:   
        main_nospin()