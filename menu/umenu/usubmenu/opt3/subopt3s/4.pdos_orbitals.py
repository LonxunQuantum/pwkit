import os
import pandas as pd 
import numpy as np
from typing import List
from pflow.io.pwmat.output.dostotalspin import Dostotalspin
from pflow.io.pwmat.output.outfermi import OutFermi
import matplotlib.pyplot as plt

from exception_decorator import dos_decorator
from exception_decorator import EnergyRangeError
from exception_decorator import Element2OrbitalFormatError


'''
Part I. no_ispin
'''
def max_and_min_nospin(df:pd.DataFrame):
    '''
    Description
    -----------
        1. 得到 `DOS.totalspin_projcted` 的能量范围
    
    Parameters
    ----------
        1. df: pd.DataFrame
            - 由 `DOS.totalspin_projected` 初始化的 pd.DataFrame 对象
    '''
    max_energy = df.loc[:, "energy"].max()
    min_energy = df.loc[:, "energy"].min()
    return max_energy, min_energy


def warm_tips_nospin(columns_lst:List[str]):
    '''
    Description
    -----------
        1. 提醒当前体系内，某原子有什么轨道
        
    Parameters
    ----------
        1. columns_lst: List[str]
            - 将 `DOS.totalspin_projected` 读成 pd.DataFrame, 
            - columns_lst 是这个 `pd.DataFrame` 的 columns 属性
    
    Return
    ------
        1. orbitals_lst: List[str]
            - e.g. ["S-3S", "S-3Px", "S-3Py", "S-3Pz", ...]
    '''
    try: 
        columns_lst.remove('energy')
    except:
        pass
    # columns_lower_lst: 轨道全是小写，处理了“输入可以是大写，也可小写”的需求
    columns_lower_lst = [value.lower() for value in columns_lst]
    
    # e.g. [ ['S', '3S'], ['S', '3Pz'], ['S', '3Px'], ... ]
    column_pairs_lst = [entry.split("-", 1) for entry in columns_lower_lst]
    # 体系中包含的元素（不重复）e.g. ['S', 'Mo']
    elements_unique_lst = list( set([tmp_pair[0] for tmp_pair in column_pairs_lst]) )
    # e.g. principle_quantum_numbers_lst: 储存了所有轨道的主量子数
    principle_quantum_numbers_lst = [int(tmp_entry[1][0]) for tmp_entry in column_pairs_lst]
    max_principle_quantum_number = max(principle_quantum_numbers_lst)
    
    ### Step 1. 获取按序排列的轨道 -- all_orbitals_lst
    ###     all_orbitals_lst: ["S-3S", "S-3Px", "S-3Py", "S-3Pz", ...]
    all_orbitals_lst = []
    for tmp_element in elements_unique_lst:
        for principle_quantum_number in range(1, max_principle_quantum_number+1):
            # direction 实际上代表 angular_quantum_number&direction
            for direction in ["s", 
                              "px", "py", "pz",
                              "dxy", "dxz", "dyz", "dz2", "d(x^2-y^2)"]:
                tmp_orbital = "{0}-{1}{2}".format(
                                            tmp_element,
                                            principle_quantum_number,
                                            direction
                                        )
                if tmp_orbital in columns_lower_lst:
                    all_orbitals_lst.append(tmp_orbital)    
    
    ### Step 2. Warm Tips:
    element2orbitals = {}
    ### Step 2.1. 初始化 `element2orbitals`
    ###         e.g. {'S': ['3S', '3Px', '3Py', '3Pz'], 'Mo': ['4S', '4Px', '4Py', '4Pz', '4Dxy', '4Dxz', '4Dyz', '4Dz2', '4D(x^2-y^2)', '5S']}
    for tmp_element in elements_unique_lst:
        element2orbitals.update({tmp_element: []})
    ### Step 2.2. 根据情况填充 `element2orbitals`
    for tmp_element in elements_unique_lst:
        for principle_quantum_number in range(1, max_principle_quantum_number+1):
            for tmp_direction in ["s", 
                                  "px", "py", "pz",
                                  "dxy", "dxz", "dyz", "dz2", "d(x^2-y^2)"]:
                tmp_orbital = "{0}-{1}{2}".format(
                                            tmp_element,
                                            principle_quantum_number,
                                            tmp_direction,
                                        )
                if tmp_orbital in all_orbitals_lst:
                    element2orbitals[tmp_element].append("{0}{1}".format(
                                                        principle_quantum_number,
                                                        tmp_direction,
                                                        )
                                                )

    ### Step 2.3. 根据 `element2orbitals` 输出
    print("+{0:-^68}+".format(" Warm Tips "))
    print(" * 存在的原子及轨道:")
    for tmp_element in list(element2orbitals.keys()):
        print("   - {0:<3}: ".format(tmp_element.capitalize()), end="")
        for tmp_orbital in element2orbitals[tmp_element]:
            print(tmp_orbital, end=", ")
        print()
    
    print("\n * 注意事项:")
    print("   - 格式: <元素>: <轨道1>, <轨道2>, ...")
    print("   - 输入“回车键”后，即可输入下一个原子以及对应轨道")
    print("   - 连续输入两次“回车键”后，开始绘制")
    print("\033[0;32m   - 示例: Mo:4d(x^2-y^2), 4dxy, 4dz2 \033[0m")
    print("+{0:-^68}+".format("---------"))
    

def get_orbitals_from_input_nospin():
    '''
    Description
    -----------
        1. 从用户输入中，得到轨道的名字
        
        # Energy  Total  S-3S  S-3Pz  S-3Px  S-3Py  Mo-4S  Mo-4Pz  Mo-4Px  Mo-4Py           
        Mo-5S   Mo-4Dz2   Mo-4Dxz   Mo-4Dyz  Mo-4D(x^2-y^2)  Mo-4Dxy

    Return
    ------
        1. columns_lower_lst: List[str]
            - 注意：列表中的元素均为小写
    
    Format
    ------
        1. Mo:4S,4Px,4Py,4Pz,4Dxy,4Dxz,4Dyz,4D(x^2-y^2)
        2. S:3S,3Px,3Py,3Pz
    '''
    columns_lower_lst = []
    element_count = 0
    while (True):
        element_count += 1
        print(" 输入绘制的原子(index={0})及轨道:".format(element_count))
        # e.g. Mo: 4dxy, 4dyz
        element_orbitals = input(" ------------>>\n")
        
        if element_orbitals == '':
            break
        
        else:
            tmp_element = element_orbitals.split(":")[0].strip().lower()
            tmp_orbitals_lst = [orbital.strip().lower() for orbital in element_orbitals.split(":")[1].split(",")]
            for tmp_orbital in tmp_orbitals_lst:
                columns_lower_lst.append( "{0}-{1}".format(tmp_element, tmp_orbital) )
            #print(tmp_orbitals_lst)
    columns_lower_lst.append("energy")
    
    return columns_lower_lst

    
@dos_decorator
def main_nospin(dos_totalspin_projected_name):
    ### Step 1. 运行 `plot_DOS_interp.x`，得到 `DOS.totalspin_projected`
    current_path = os.getcwd()
    dos_totalspin_projected_path = os.path.join(
                                    current_path,
                                    dos_totalspin_projected_name,
                                    )
    
    ### Note: `module load mkl/latest`
    returncode = os.system("module load mkl/latest > /dev/null")
    if returncode != 0:
        print("Warning: Can't load MKL module")
    os.system('plot_DOS_interp.x > /dev/null')
    
    
    ### Step 2. 用 `DOS.totalspin_project` 初始化 `Dostotalspin` 对象
    dos_totalspin_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_totalspin_projected_path
                                )
    df_orbitals = dos_totalspin_projected_object.get_pdos_orbitals()
    ### 将列全换成小写
    df_orbitals.columns = [column.lower() for column in df_orbitals.columns]
    
    ### Step 2.1. 若存在 OUT.FERMI，则减去费米能级
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        output_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = output_fermi_object.get_efermi()
        df_orbitals.loc[:, "energy"] =  df_orbitals.loc[:, "energy"] - efermi_ev
    
    
    ### Step 3. 获取绘制的能量范围
    ### Step 3.1. 得到能量的范围 -- [e_min_value, e_max_value]
    e_max_value, e_min_value = max_and_min_nospin(df_orbitals)
    e_max_value = np.round(e_max_value, 4)
    e_min_value = np.round(e_min_value, 4)
    
    
    ### Step 3.2. 输入需要绘制原子及其轨道 -- mask_element_orbitals
    warm_tips_nospin(columns_lst=df_orbitals.columns.to_list())
    try:
        mask_element_orbitals = get_orbitals_from_input_nospin()
    except IndexError as ie:
        raise Element2OrbitalFormatError("未输入:和轨道名称")
        
    #print(mask_element_orbitals)
    
    ### Step 3.3. 输入能量的范围
    print(" 能量范围是 {0} eV ~ {1} eV。输入绘制的能量范围 (e.g. -2,2)".format(e_min_value, e_max_value))
    e_range_str = input(" ------------>>\n")
    e_max = float( e_range_str.split(',')[1].strip() )
    e_min = float( e_range_str.split(',')[0].strip() )
    if (e_max > e_max_value) or (e_min < e_min_value):
        #print('\n\033[0;31m Error: 超出能量范围! \033[0m')
        raise EnergyRangeError("超出能量范围")
    
    ### Step 3.4. 根据输入的能量范围筛选数据 -- `df_elements_plot`
    mask = (df_orbitals.loc[:, "energy"] < e_max) & \
            (df_orbitals.loc[:, "energy"] > e_min)
    df_orbitals_plot = df_orbitals.loc[mask, :]
    
    ### Step 3.5. 根据用户的输入筛选数据 (e.g. "Mo:4S,4Px,4Py,4Pz,4Dxy,4Dxz,4Dyz,4D(x^2-y^2)")
    # Step 3.2 :warm_tips(columns_lst=df_orbitals_plot.columns.to_list()) 
    try:
        df_orbitals_plot = df_orbitals_plot.loc[:, mask_element_orbitals]
    except KeyError as ke:
        raise Element2OrbitalFormatError("未输入轨道名称 or 轨道名称错误")
    
    
    ### Step 4. 绘制图像
    plot_pdos_orbitals_nospin(
                    df_pdos_orbitals=df_orbitals_plot,
                    E_min=e_min,
                    E_max=e_max,
                    efermi_ev=efermi_ev,
                    )
    
    ### Step 5. 输出总结
    print_sum_nospin(efermi_ev=efermi_ev)
    
    

def plot_pdos_orbitals_nospin(
                df_pdos_orbitals:pd.DataFrame,
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
    for idx, tmp_column in enumerate(df_pdos_orbitals.columns.to_list()):
        if tmp_column == "energy":
            continue
        plt.plot(
                df_pdos_orbitals.loc[:, "energy"],
                df_pdos_orbitals.loc[:, tmp_column],                
                c=colors_lst[idx],
                lw="2",
                label=tmp_column.capitalize(),
                )
    
    # 1. xlabel / ylabel
    plt.xlabel("energy (eV)",
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
                frameon=False,
                loc=(0.6, 0.6))

    # 6. 保存图片
    if efermi_ev:
        output_jpg_path = os.path.join(current_path, "dos_orbitals_ShiftFermi.jpg")
        output_csv_path = os.path.join(current_path, "dos_orbitals_ShiftFermi.csv")
        df_pdos_orbitals.to_csv(
                        output_csv_path,
                        sep=",",
                        index=False)
    else:
        output_jpg_path = os.path.join(current_path, "dos_orbitals.jpg")
        output_csv_path = os.path.join(current_path, "dos_orbitals.csv")
        df_pdos_orbitals.to_csv(
                        output_csv_path,
                        sep=",",
                        index=False)
    plt.savefig(
            output_jpg_path,
            dpi=300,
            bbox_inches="tight",
            )


def print_sum_nospin(efermi_ev:float):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输出文件:", end="")
    if efermi_ev:
        print("\t - {0}".format("dos_orbitals_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_orbitals_ShiftFermi.jpg"))
    else:
        print("\t - {0}".format("dos_orbitals.csv"))
        print("\t\t\t - {0}".format("dos_orbitals.jpg"))
    if not efermi_ev:
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[0;31m \t* 当前目录下没有 OUT.FERMI 文件，态密度没有减去费米能级!\033[0m\n", end="")

    print("*{0:-^68}*".format("---------"))



'''
Part II. ispin
'''
def max_and_min_spin(
                df_up:pd.DataFrame,
                df_down:pd.DataFrame,
                ):
    '''
    Description
    -----------
        1. 得到 `DOS.totalspin_projcted` 的能量范围
    
    Parameters
    ----------
        1. df: pd.DataFrame
            - 由 `DOS.totalspin_projected` 初始化的 pd.DataFrame 对象
    '''
    max_energy_up = df_up.loc[:, "energy"].max()
    min_energy_up = df_up.loc[:, "energy"].min()

    max_energy_down = df_down.loc[:, "energy"].max()
    min_energy_down = df_down.loc[:, "energy"].min()
    
    max_energy = max([max_energy_up, max_energy_down])
    min_energy = min([min_energy_up, min_energy_down])
    
    return max_energy, min_energy



def warm_tips_spin(columns_lst:List[str]):
    '''
    Description
    -----------
        1. 提醒当前体系内，某原子有什么轨道
        
    Parameters
    ----------
        1. columns_lst: List[str]
            - 将 `DOS.totalspin_projected` 读成 pd.DataFrame, 
            - columns_lst 是这个 `pd.DataFrame` 的 columns 属性
    
    Return
    ------
        1. orbitals_lst: List[str]
            - e.g. ["S-3S", "S-3Px", "S-3Py", "S-3Pz", ...]
    '''
    try: 
        columns_lst.remove('energy')
    except:
        pass
    # columns_lower_lst: 轨道全是小写，处理了“输入可以是大写，也可小写”的需求
    columns_lower_lst = [value.lower() for value in columns_lst]
    
    # e.g. [ ['S', '3S'], ['S', '3Pz'], ['S', '3Px'], ... ]
    column_pairs_lst = [entry.split("-", 1) for entry in columns_lower_lst]
    # 体系中包含的元素（不重复）e.g. ['S', 'Mo']
    elements_unique_lst = list( set([tmp_pair[0] for tmp_pair in column_pairs_lst]) )
    # e.g. principle_quantum_numbers_lst: 储存了所有轨道的主量子数
    principle_quantum_numbers_lst = [int(tmp_entry[1][0]) for tmp_entry in column_pairs_lst]
    max_principle_quantum_number = max(principle_quantum_numbers_lst)
    
    ### Step 1. 获取按序排列的轨道 -- all_orbitals_lst
    ###     all_orbitals_lst: ["S-3S", "S-3Px", "S-3Py", "S-3Pz", ...]
    element2orbitals = {}
    ### Step 2.1. 初始化 `element2orbitals`
    ###         e.g. {'S': ['3S', '3Px', '3Py', '3Pz'], 'Mo': ['4S', '4Px', '4Py', '4Pz', '4Dxy', '4Dxz', '4Dyz', '4Dz2', '4D(x^2-y^2)', '5S']}
    for tmp_element in elements_unique_lst:
        element2orbitals.update({tmp_element: []})
    ### Step 2.2. 根据情况填充 `element2orbitals`
    for tmp_element in elements_unique_lst:
        for principle_quantum_number in range(1, max_principle_quantum_number+1):
            # direction 实际上代表 angular_quantum_number&direction
            for direction in ["s", 
                              "px", "py", "pz",
                              "dxy", "dxz", "dyz", "dz2", "d(x^2-y^2)"]:
                tmp_orbital = "{0}-{1}{2}".format(
                                            tmp_element,
                                            principle_quantum_number,
                                            direction
                                        )
                if tmp_orbital in columns_lower_lst:
                    element2orbitals[tmp_element].append("{0}{1}".format(
                                                                    principle_quantum_number,
                                                                    direction,
                                                                    )
                                                    ) 

    ### Step 2.3. 根据 `element2orbitals` 输出
    print("+{0:-^68}+".format(" Warm Tips "))
    print(" * 存在的原子及轨道:")
    for tmp_element in list(element2orbitals.keys()):
        print("   - {0:<3}: ".format(tmp_element.capitalize()), end="")
        for tmp_orbital in element2orbitals[tmp_element]:
            print(tmp_orbital, end=", ")
        print()
    
    print("\n * 注意事项:")
    print("   - 格式: <元素>: <轨道1>, <轨道2>, ...")
    print("   - 输入“回车键”后，即可输入下一个原子以及对应轨道")
    print("   - 连续输入两次“回车键”后，开始绘制")
    print("\033[0;32m    - 示例: Mo:4d(x^2-y^2), 4dxy, 4dz2 \033[0m")
    print("+{0:-^68}+".format("---------"))



def get_orbitals_from_input_spin():
    '''
    Description
    -----------
        1. 从用户输入中，得到轨道的名字
        
        # Energy  Total  S-3S  S-3Pz  S-3Px  S-3Py  Mo-4S  Mo-4Pz  Mo-4Px  Mo-4Py           
        Mo-5S   Mo-4Dz2   Mo-4Dxz   Mo-4Dyz  Mo-4D(x^2-y^2)  Mo-4Dxy

    Return
    ------
        1. columns_lower_lst: List[str]
            - 注意：列表中的元素均为小写
    
    Format
    ------
        1. Mo:4S,4Px,4Py,4Pz,4Dxy,4Dxz,4Dyz,4D(x^2-y^2)
        2. S:3S,3Px,3Py,3Pz
    '''
    columns_lower_lst = []
    element_count = 0
    while (True):
        element_count += 1
        print(" 输入绘制的原子(index={0})及轨道:".format(element_count))
        # e.g. Mo: 4dxy, 4dyz
        element_orbitals = input(" ------------>>\n")
        if element_orbitals == '':
            break
        else:
            tmp_element = element_orbitals.split(":")[0].strip().lower()
            tmp_orbitals_lst = [orbital.strip().lower() for orbital in element_orbitals.split(":")[1].split(",")]
            for tmp_orbital in tmp_orbitals_lst:
                columns_lower_lst.append( "{0}-{1}".format(tmp_element, tmp_orbital) )
    columns_lower_lst.append("energy")
    
    return columns_lower_lst



@dos_decorator
def main_spin(
            dos_spinup_projected_name:str,
            dos_spindown_projected_name:str,
            ):
    ### Step 1. 运行 `plot_DOS_interp.x`，得到 `DOS.spinup_projected`和`DOS.spindown_projected`
    current_path = os.getcwd()
    dos_spinup_projected_path = os.path.join(
                                    current_path,
                                    dos_spinup_projected_name,
                                )
    dos_spindown_projected_path = os.path.join(
                                    current_path,
                                    dos_spindown_projected_name,
                                )
    ### Note: `module load mkl/latest`
    returncode = os.system("module load mkl/latest > /dev/null")
    if returncode != 0:
        print("Warning: Can't load MKL module")
    os.system('plot_DOS_interp.x > /dev/null')
    
    
    ### Step 2. 用 `DOS.totalspin_project` 初始化 `Dostotalspin` 对象
    dos_spinup_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_spinup_projected_path
                                )
    dos_spindown_projected_object = Dostotalspin(
                                dos_totalspin_path=dos_spindown_projected_path
                                )
    
    df_spinup_orbitals = dos_spinup_projected_object.get_pdos_orbitals()
    df_spindown_orbitals = dos_spindown_projected_object.get_pdos_orbitals()
    ### 将列全换成小写
    df_spinup_orbitals.columns = [column.lower() for column in df_spinup_orbitals.columns]
    df_spindown_orbitals.columns = [column.lower() for column in df_spindown_orbitals.columns]
    
    ### Step 2.1. 若存在 OUT.FERMI，则减去费米能级
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    efermi_ev = False
    if os.path.exists(out_fermi_path):
        output_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
        efermi_ev = output_fermi_object.get_efermi()
        df_spinup_orbitals.loc[:, "energy"] =  df_spinup_orbitals.loc[:, "energy"] - efermi_ev
        df_spindown_orbitals.loc[:, "energy"] =  df_spindown_orbitals.loc[:, "energy"] - efermi_ev
    
    
    ### Step 3. 获取绘制的能量范围
    ### Step 3.1. 得到能量的范围 -- [e_min_value, e_max_value]
    e_max_value, e_min_value = max_and_min_spin(
                                    df_up=df_spinup_orbitals,
                                    df_down=df_spindown_orbitals,
                                )
    e_max_value = np.round(e_max_value, 4)
    e_min_value = np.round(e_min_value, 4)
    
    
    ### Step 3.2. 输入需要绘制原子及其轨道 -- mask_element_orbitals
    warm_tips_nospin(columns_lst=df_spinup_orbitals.columns.to_list())
    try:
        mask_element_orbitals = get_orbitals_from_input_nospin()
    except IndexError as ie:
        raise Element2OrbitalFormatError("未输入:和轨道名称")
    
    
    ### Step 3.3. 输入能量的范围
    print(" 能量范围是 {0} eV ~ {1} eV。输入绘制的能量范围 (e.g. -2,2)".format(e_min_value, e_max_value))
    e_range_str = input(" ------------>>\n")
    e_max = float( e_range_str.split(',')[1].strip() )
    e_min = float( e_range_str.split(',')[0].strip() )
    if (e_max > e_max_value) or (e_min < e_min_value):
        #print('\n\033[0;31m Error: 超出能量范围! \033[0m')
        raise EnergyRangeError("超出能量范围")
    
    ### Step 3.4. 根据输入的能量范围筛选数据 -- `df_elements_plot`
    mask_spinup = (df_spinup_orbitals.loc[:, "energy"] < e_max) & \
                (df_spinup_orbitals.loc[:, "energy"] > e_min)
    df_spinup_orbitals_plot = df_spinup_orbitals.loc[mask_spinup, :]
    mask_spindown = (df_spindown_orbitals.loc[:, "energy"] < e_max) & \
                (df_spindown_orbitals.loc[:, "energy"] > e_min)
    df_spindown_orbitals_plot = df_spindown_orbitals.loc[mask_spindown, :]

    ### Step 3.5. 根据用户的输入筛选数据 (e.g. "Mo:4S,4Px,4Py,4Pz,4Dxy,4Dxz,4Dyz,4D(x^2-y^2)")
    # Step 3.2 :warm_tips(columns_lst=df_orbitals_plot.columns.to_list()) 
    try:
        df_spinup_orbitals_plot = df_spinup_orbitals_plot.loc[:, mask_element_orbitals]
        df_spindown_orbitals_plot = df_spindown_orbitals_plot.loc[:, mask_element_orbitals]
    except KeyError as ke:
        raise Element2OrbitalFormatError("未输入轨道名称 or 轨道名称错误")
    
    ### Step 4. 绘制图像
    plot_pdos_orbitals_spin(
                df_pdos_spinup_orbitals=df_spinup_orbitals_plot,
                df_pdos_spindown_orbitals=df_spindown_orbitals_plot,
                E_min=e_min,
                E_max=e_max,
                efermi_ev=efermi_ev,
                )
    
    ### Step 5. 输出总结
    print_sum_spin(efermi_ev=efermi_ev)
    
    
def plot_pdos_orbitals_spin(
                df_pdos_spinup_orbitals:pd.DataFrame,
                df_pdos_spindown_orbitals:pd.DataFrame,
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
    plt.axhline(y=0, c="black", lw=1.5)
    for tmp_spin, tmp_df_pdos_orbitals in zip(
                                ["up", "down"],
                                [df_pdos_spinup_orbitals, df_pdos_spindown_orbitals],
                            ):
        for idx, tmp_column in enumerate(tmp_df_pdos_orbitals.columns.to_list()):
            if tmp_column == "energy":
                continue
            if tmp_spin == "down":
                color_idx = df_pdos_spinup_orbitals.shape[1] - 1 + idx
            else:
                color_idx = idx
            plt.plot(
                    tmp_df_pdos_orbitals.loc[:, "energy"],
                    tmp_df_pdos_orbitals.loc[:, tmp_column],                
                    c=colors_lst[color_idx],
                    lw="2",
                    label="{0}_{1}".format(tmp_column.capitalize(), tmp_spin),
                    )
    
    # 1. xlabel / ylabel
    plt.xlabel("energy (eV)",
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
                frameon=False,
                loc="upper right",
                )

    # 6. 保存图片
    if efermi_ev:
        output_jpg_path = os.path.join(current_path, "dos_orbitals_ShiftFermi.jpg")
        output_csv_spinup_path = os.path.join(current_path, "dos_spinup_orbitals_ShiftFermi.csv")
        output_csv_spindown_path = os.path.join(current_path, "dos_spindown_orbitals_ShiftFermi.csv")        
        
        df_pdos_spinup_orbitals.to_csv(
                        output_csv_spinup_path,
                        sep=",",
                        index=False)
        df_pdos_spinup_orbitals.to_csv(
                        output_csv_spindown_path,
                        sep=",",
                        index=False)
    else:
        output_jpg_path = os.path.join(current_path, "dos_orbitals.jpg")
        output_csv_spinup_path = os.path.join(current_path, "dos_spinup_orbitals.csv")
        output_csv_spindown_path = os.path.join(current_path, "dos_spindown_orbitals.csv")        
        
        df_pdos_spinup_orbitals.to_csv(
                        output_csv_spinup_path,
                        sep=",",
                        index=False)
        df_pdos_spinup_orbitals.to_csv(
                        output_csv_spindown_path,
                        sep=",",
                        index=False)
        
    plt.savefig(
            output_jpg_path,
            dpi=300,
            bbox_inches="tight",
            )

    
def print_sum_spin(efermi_ev:float):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输出文件:", end="")
    if efermi_ev:
        print("\t - {0}".format("dos_spinup_orbitals_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_spindown_orbitals_ShiftFermi.csv"))
        print("\t\t\t - {0}".format("dos_orbitals_ShiftFermi.jpg"))
    else:
        print("\t - {0}".format("dos_spinup_orbitals.csv"))
        print("\t - {0}".format("dos_spindown_orbitals.csv"))
        print("\t\t\t - {0}".format("dos_orbitals.jpg"))
    if not efermi_ev:
        print("*{0:-^68}*".format("---------"), end="")
        print("\n\033[0;31m \t* 当前目录下没有 OUT.FERMI 文件，态密度没有减去费米能级!\033[0m\n", end="")

    print("*{0:-^68}*".format("---------"))




'''
Part III. Driver code
'''
if __name__ == "__main__":
    ### Step 1. 如果没有 DOS.input，直接报错
    current_path = os.getcwd()
    dos_input_path = os.path.join(current_path, "DOS.input")
    if not os.path.exists(dos_input_path):
        print("\033[0;31m+{0:-^60}+\033[0m".format(" Error "))
        print('\033[0;31m\t* 请先使用PWkit生成 DOS.input 文件!\033[0m')
        print("\033[0;31m+{0:-^60}+\033[0m".format(""))
        raise SystemExit
        
        
    ### Step 2. 绘制图像
    dos_totalspin_projected_name = "DOS.totalspin_projected"
    dos_spinup_projected_name = "DOS.spinup_projected"
    dos_spindown_projected_name = "DOS.spindown_projected"

    dos_spinup_path = os.path.join(current_path, "DOS.spinup")
    dos_spindown_path = os.path.join(current_path, "DOS.spindown")
    
    # mark_spin: True--打开自旋，False--关闭自旋
    mark_spin = os.path.exists(dos_spinup_path) and os.path.exists(dos_spindown_path)
    
    if mark_spin:
        main_spin(
                dos_spinup_projected_name=dos_spinup_projected_name,
                dos_spindown_projected_name=dos_spindown_projected_name,
                )
    else:
        main_nospin(
                dos_totalspin_projected_name=dos_totalspin_projected_name,
                )