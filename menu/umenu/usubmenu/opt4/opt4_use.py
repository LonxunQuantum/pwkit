import os
import numpy as np
import matplotlib.pyplot as plt

from typing import Dict, List
from pflow.io.pwmat.output.report import Report
from pflow.io.pwmat.input.inkpt import Inkpt


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


### Step 4. 


### Step 5. 绘制图像
def plot_band(
            xs_lst:List[float],
            yss_dict:Dict[str, np.ndarray],
            hsp_names_lst:List[str],
            hsp_xs_lst:List[float],
            ):
    colors_lst = ["steelblue", "red"]
    band_png_path = os.path.join(current_path, "bandstructure.png")
    plt.figure(figsize=(10, 8))
    
    
    for idx_band in range(yss_dict["up"].shape[1]):
        ys_array = yss_dict["up"].transpose()   # 1d:band 索引; 2d:kpoints 索引
        plt.plot(xs_lst, ys_array[idx_band],
                c=colors_lst[0])
        plt.scatter(xs_lst, ys_array[idx_band],
                c=colors_lst[0])
    
    plt.ylim(-5, 5)
    plt.savefig(band_png_path)


if __name__ == "__main__":
    # 0. 文件路径
    current_path = os.getcwd()
    in_kpt_path = os.path.join(current_path, "IN.KPT")
    report_path = os.path.join(current_path, "REPORT")
    atom_config_path = os.path.join(current_path, "final.config")
    
    # 1. xs_lst: List[int]
    xs_lst = get_xs_lst(
                    in_kpt_path=in_kpt_path,
                    atom_config_path=atom_config_path)
    
    # 2. yss_dict
    yss_dict = get_yss_dict(report_path=report_path)
    assert (len(xs_lst) == yss_dict["up"].shape[0])
    
    # 3. hsp_names_lst, hsp_xs_lst
    hsp_names_lst, hsp_xs_lst = get_hsp(
                                    in_kpt_path=in_kpt_path,
                                    atom_config_path=atom_config_path,
                                    )
    
    # 4. 利用上述信息，绘制能带图像
    plot_band(
            xs_lst=xs_lst, 
            yss_dict=yss_dict,
            hsp_names_lst=hsp_names_lst,
            hsp_xs_lst=hsp_xs_lst)