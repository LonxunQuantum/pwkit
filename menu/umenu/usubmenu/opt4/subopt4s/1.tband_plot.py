import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from typing import Dict, List, Union
from pflow.io.pwmat.output.report import Report
from pflow.io.pwmat.input.inkpt import Inkpt
from pflow.io.pwmat.output.outfermi import OutFermi

from band_decorator import band_decorator
from band_decorator import EnergyRangeError
from band_decorator import EnergyRangeFormatError


### Step 1. 得到能带的横坐标 (unit: 埃)
def get_xs_lst(
            in_kpt_path:str,
            atom_config_path:str,
            ):
    '''
    Description
    -----------
        1. 得到所有 kpoints 距离gamma点的kpath距离。用作 bandstructure 的横坐标
    
    Parameters
    ----------
        1. in_kpt_path: str
            - IN.KPT 文件的路径
        2. atom_config_path: str
            - atom.config 文件的路径
    
    Return
    ------
        1. distances_from_gamma: List[float]
            - bandstructure 的横坐标
    '''
    in_kpt_object = Inkpt(in_kpt_path=in_kpt_path)
    distances_from_gamma = \
            in_kpt_object.get_distance_from_gamma_A(atom_config_path=atom_config_path)
    return distances_from_gamma


### Step 2. 得到能带的纵坐标 (unit: eV)
def get_yss_dict(report_path:str):
    '''
    Description
    -----------
        1. 得到能带的纵坐标 (所有kpoints的本征值)
    
    Return
    ------
        1. spin2eign_energies: Dict[str, np.ndarray]
    '''
    report_object = Report(report_path=report_path)
    spin2eigen_energies:Dict[str:np.ndarray] = report_object.get_eigen_energies()
    return spin2eigen_energies


### Step 3. 得到高对称点的名称和坐标
def get_hsp(
        in_kpt_path:str,
        atom_config_path:str):
    '''
    Description
    -----------
        1. 得到对称点的`名称`和`距gamma的距离（unit: 埃）`
    
    Return
    ------
        1. hsp_names_lst: List[str]
            - 高对称点的名字
        2. hsp_xs_lst: List[float]
            - 高对称点的横坐标 (在 bandstructure 上)
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


### Step 4. 费米能级
def get_fermi(out_fermi_path:str):
    '''
    Description
    -----------
        1. 从 OUT.FERMI 中读取费米能级 (unit: eV)
    '''
    out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
    efermi = out_fermi_object.get_efermi()
    
    return efermi


### Step 5. 绘制图像
def plot_band(
            xs_lst:List[float],
            yss_dict:Dict[str, np.ndarray],
            hsp_names_lst:List[str],
            hsp_xs_lst:List[float],
            efermi_ev:Union[bool, float],
            E_min:float,
            E_max:float,
            band_png_path:str,
            ):
    ### Step 0. 颜色选择、输出文件的路径、图
    colors_lst = ["steelblue", "coral"]
    band_png_path = band_png_path
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
    
    ### Step 1. 若存在 OUT.FERMI 文件，则所有本征能量需要减去费米能级
    if (efermi_ev != False):
        yss_dict["up"] -= efermi_ev
        if (yss_dict["down"].size != 0):
            yss_dict["down"] -= efermi_ev
    
    ### Step 2. 处理数据的部分
    ### Step 2.2. spinup
    for idx_band in range(yss_dict["up"].shape[1]):
        ys_array = yss_dict["up"].transpose()   # 1d:band 索引; 2d:kpoints 索引
        plt.plot(xs_lst, ys_array[idx_band],
                c=colors_lst[0],
                lw=2,
                alpha=0.8,
                )
        #plt.scatter(xs_lst, ys_array[idx_band],
        #        c=colors_lst[0],
        #        alpha=0.8)
    ### Step 2.2. spindown
    if (yss_dict["down"].size != 0):
        for idx_band in range(yss_dict["down"].shape[1]):
            ys_array = yss_dict["down"].transpose()   # 1d:band 索引; 2d:kpoints 索引
            plt.plot(xs_lst, ys_array[idx_band],
                    c=colors_lst[1],
                    lw=2,
                    alpha=0.6,
                    )
            #plt.scatter(xs_lst, ys_array[idx_band],
            #        c=colors_lst[1],
            #        alpha=0.6)
        
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
    ax.set_xticks(hsp_xs_lst, )
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
                color="black")
    
    # 7. xrange / yrange
    plt.xlim(0, max(xs_lst))
    plt.ylim(E_min, E_max)
    
    # 8. legend
    if (yss_dict["down"].size != 0):
        line1 = Line2D([0], [0], color='steelblue', linewidth=2.5, linestyle='-')
        line2 = Line2D([0], [0], color='coral', linewidth=2.5, linestyle='-')
        legend_font = {"size" : 18, 
                        "weight": "bold"
                        }
        legend_handles = [line1, line2]
        legend_labels = ['spin_up', 'spin_down']
        ax.legend(legend_handles, legend_labels, 
                prop=legend_font,
                frameon=False)

    # 9. 保存图片
    plt.savefig(band_png_path,
                dpi=300,
                bbox_inches="tight",)


def print_sum(efermi_ev:Union[float, bool]): 
    print("*{0:-^68}*".format( " Summary "))
    
    print("\t* 输入文件:", end='\t')
    print(" - {0}".format("final.config"))
    print(" \t\t\t - {0}".format("IN.KPT"))
    print(" \t\t\t - {0}".format("REPORT"))
    if (efermi_ev != False):
        print(" \t\t\t - {0}".format("OUT.FERMI"))
    
    print("\t* 输出文件:", end='\t')
    if (efermi_ev == False):
        print(" - {0}".format("bandstructure.png"))
    else:
        print(" - {0}".format("bandstructure_ShiftFermi.png"))

    # Warning: 
    if (efermi_ev == False):
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[1;31m \t* 当前目录下没有 OUT.FERMI 文件，能带没有减去费米能级!\033[0m\n", end="")
    
    print("*{0:-^68}*".format("---------"))



@band_decorator
def main():
    # 0. 文件路径
    current_path = os.getcwd()
    in_kpt_path = os.path.join(current_path, "IN.KPT")
    report_path = os.path.join(current_path, "REPORT")
    atom_config_path = os.path.join(current_path, "final.config")
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    band_png_path = os.path.join(current_path, "bandstructure.png")
    
    # 1. 若当前目录下存在 OUT.FERMI，则所有本征能量需要减去费米能级
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        efermi_ev = get_fermi(out_fermi_path=out_fermi_path)
        band_png_path = os.path.join(current_path, "bandstructure_ShiftFermi.png")    

    # 2. xs_lst: List[int]
    xs_lst = get_xs_lst(
                    in_kpt_path=in_kpt_path,
                    atom_config_path=atom_config_path)
    
    # 3. yss_dict
    yss_dict = get_yss_dict(report_path=report_path)
    assert (len(xs_lst) == yss_dict["up"].shape[0])
    #print(yss_dict)
    
    # 3.1. 输入能带的范围
    yss_dict_ = {"up":np.array([]), "down":np.array([])}
    if efermi_ev:
        yss_dict_["up"] = yss_dict["up"] - efermi_ev
        if (yss_dict["down"].size != 0):
            yss_dict_["down"] = yss_dict["down"] - efermi_ev
    else:
        yss_dict_["up"] = yss_dict["up"]
        if (yss_dict["down"].size != 0):
            yss_dict_["down"] = yss_dict["down"]
    #print(yss_dict_)
    
    if yss_dict["down"].size == 0:  # ispin 关闭
        e_max = np.max(yss_dict_["up"])
        e_min = np.min(yss_dict_["up"])
    else:
        e_max = max( [np.max(yss_dict_["up"]), np.max(yss_dict_["down"])] )
        e_min = min( [np.min(yss_dict_["up"]), np.min(yss_dict_["down"])] )
    input_string = input(
        "\n能量范围是 {0} eV ~ {1} eV。请输入绘制的能量范围 (e.g. -5,5)\n ------------>>\n".format(
        round(e_min, 3),
        round(e_max, 3),
        ))
    try:
        E_min = float( input_string.split(",")[0] )
        E_max = float( input_string.split(",")[1] )
    except:
        raise EnergyRangeFormatError("能量范围的格式错误")
    
    if (E_min < e_min) or (E_max > e_max): 
        raise EnergyRangeError("输入的能量区间过大")
    
    # 4. hsp_names_lst, hsp_xs_lst
    hsp_names_lst, hsp_xs_lst = get_hsp(
                                    in_kpt_path=in_kpt_path,
                                    atom_config_path=atom_config_path,
                                    )
    
    # 5. 利用上述信息，绘制能带图像
    plot_band(
            xs_lst=xs_lst, 
            yss_dict=yss_dict,
            hsp_names_lst=hsp_names_lst,
            hsp_xs_lst=hsp_xs_lst,
            efermi_ev=efermi_ev,
            E_min=E_min,
            E_max=E_max,
            band_png_path=band_png_path,
            )
    
    print_sum(efermi_ev=efermi_ev)
    
    
if __name__ == "__main__":
    main()