import os 
import math
import linecache

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List


# REPORT 中每行写 5 个 eigen energies
NUM_PER_LINE = 5


def search_aim(file_path:str, aim_content:str):
    '''
    Description
    -----------
        1. 查询文件中是否存在特定内容(aim_content)，并确定所在的行数
    
    Parameters
    ----------
        1. file_path: str
            - 在此处特指 REPORT
        2. aim_content: str
    '''
    with open(file_path, "r") as f:
        lines_lst = f.readlines()
    
    idxs_lst = []
    for idx, line in enumerate(lines_lst, 1):
        if aim_content in line:
            idxs_lst.append(idx)
        
    return idxs_lst


def get_xaxis_from_inkpt(
                    in_kpt_path:str,
                    report_path:str,
                    ):
    '''
    Description
    -----------
        1. 从 IN.KPT 和 REPORT 中读取 bandstructure 的横坐标
        2. Note: IN.KPT 和 REPORT 中的kpoints坐标不完全一样
        
    Parameters
    ----------
        1. kpoints_coords: np.ndarray
            kpoints 的坐标
    
    Return
    ------
        1. distances_from_gamma_lst: List[float]
            - 能带的横坐标
        2. hsp_names_lst: List[str]
            - 高对称点的名字
        3. hsp_xvalue_lst: List[float]
            - 高对称点在 bandstructure 图上的横坐标
    '''
    ### Step 1. 得到 kpoints 的坐标、高对称点的行索引、高对称点的名字
    with open(in_kpt_path, "r") as f:
        lines_lst = f.readlines()
    kpts_lst = [line.split() for line in lines_lst][2:]
    idxs_for_hsp = [kpts_lst.index(tmp_kpt, tmp_idx, len(kpts_lst)) for tmp_idx, tmp_kpt in enumerate(kpts_lst) if (len(tmp_kpt)==5)]
    names_for_hsp = [kpts_lst[kpts_lst.index(tmp_kpt, tmp_idx, len(kpts_lst))][-1] for tmp_idx, tmp_kpt in enumerate(kpts_lst) if (len(tmp_kpt)==5)]
    
    ### Step 1.1. 得到 kpt_coords_array:np.ndarray -- 所有 kpoints 的分数坐标
    num_kpts = len(kpts_lst)
    with open(report_path, "r") as f:
        lines_lst = f.readlines()
    idx_start = search_aim(file_path=report_path, aim_content="total number of K-point:")[0]
    kpt_coords_lst = []
    for tmp_line in lines_lst[idx_start:idx_start+num_kpts]:
        tmp_coord = [float(value) for value in tmp_line.split()]
        kpt_coords_lst.append(tmp_coord)
    kpt_coords_array = np.array(kpt_coords_lst)
    
    ### Step 1.2. 得到 hsp_idx2name: Dict[int, str] -- 高对称点的索引和名字
    hsp_idx2name = {}   # Dict[int, str] - e.g. {高对称的行索引: 高对称点的名字}
    for tmp_idx, tmp_name in zip(idxs_for_hsp, names_for_hsp):
        hsp_idx2name.update({tmp_idx: tmp_name})
    #print(hsp_idx2name)
    
    ### Step 2. 得到kpoints之间的距离: distances_array
    distances_lst = list( np.linalg.norm( np.diff(kpt_coords_array, axis=0), axis=1) )
    distances_lst.insert(0, 0)
    distances_array = np.array(distances_lst)
    #print(len(distances_array))
    
    ### Step 3. 截断不同的 kpath -- cutoff_idx_pairs_lst
    cutoff_idx_lst = []   # [0, 58, 59, 63, 64, 68] -> [[0, 58], [59, 63], [64, 68]]
    hsp_idxs_lst = sorted(hsp_idx2name.keys())  # e.g. [0, 10, 16, 27, 31, 41, 47, 58, 59, 63, 64, 68]
    
    ### Step 3.1. 得到 [0, 58, 59, 63, 64, 68]
    for tmp_idx in range(1, len(hsp_idxs_lst)):
        if ((hsp_idxs_lst[tmp_idx] - hsp_idxs_lst[tmp_idx-1]) == 1):
            cutoff_idx_lst.append(hsp_idxs_lst[tmp_idx-1])
            cutoff_idx_lst.append(hsp_idxs_lst[tmp_idx])    # [58, 59, 63, 64]
    cutoff_idx_lst.insert(0, 0) # [0, 58, 59, 63, 64]
    cutoff_idx_lst.append(len(kpt_coords_array)-1)    # [0, 58, 59, 63, 64, 68]
    #print(cutoff_idx_lst)
    
    ### Step 3.2. 得到 `[0, 58, 59, 63, 64, 68] -> [[0, 58], [59, 63], [64, 68]]`
    cutoff_idxs_pair_lst = []
    for tmp_idx in range(1, len(cutoff_idx_lst), 2):
        tmp_pair = [cutoff_idx_lst[tmp_idx-1], cutoff_idx_lst[tmp_idx]+1]   # Python 索引包括前、不包括后
        cutoff_idxs_pair_lst.append(tmp_pair)
    
    ### Step 4. 计算 bandstructure 的横坐标
    '''
    e.g.
    ----
    1. kpaths_distances_from_gamma_lst
    -------------------------------
        [0, 58]
        [0.         0.05       0.1        0.15       0.2        0.25
        0.3        0.35       0.4        0.45       0.5        0.5621135
        0.6242261  0.6863387  0.74845175 0.81056525 0.87267785 0.91553276
        0.95838767 1.00124259 1.0440975  1.08695242 1.12980733 1.17266224
        1.21551716 1.25837207 1.30122698 1.3440819  1.4690819  1.5940819
        1.7190819  1.8440819  1.8940819  1.9440819  1.9940819  2.0440819
        2.0940819  2.1440819  2.1940819  2.2440819  2.2940819  2.3440819
        2.40619539 2.46830799 2.5304206  2.59253365 2.65464714 2.71675974
        2.75961466 2.80246957 2.84532448 2.8881794  2.93103431 2.97388923
        3.01674414 3.05959905 3.10245397 3.14530888]
        
        [59, 63]
        [0.5   0.625 0.75  0.875]
        
        [64, 68]
        [0.37267785 0.49767785 0.62267785 0.74767785]
        
    2. new_kpaths_distances_from_gamma_lst
    --------------------------------------
        [array([0.        , 0.05      , 0.1       , 0.15      , 0.2       ,
            0.25      , 0.3       , 0.35      , 0.4       , 0.45      ,
            0.5       , 0.5621135 , 0.6242261 , 0.6863387 , 0.74845175,
            0.81056525, 0.87267785, 0.91553276, 0.95838767, 1.00124259,
            1.0440975 , 1.08695242, 1.12980733, 1.17266224, 1.21551716,
            1.25837207, 1.30122698, 1.3440819 , 1.4690819 , 1.5940819 ,
            1.7190819 , 1.8440819 , 1.8940819 , 1.9440819 , 1.9940819 ,
            2.0440819 , 2.0940819 , 2.1440819 , 2.1940819 , 2.2440819 ,
            2.2940819 , 2.3440819 , 2.40619539, 2.46830799, 2.5304206 ,
            2.59253365, 2.65464714, 2.71675974, 2.75961466, 2.80246957,
            2.84532448, 2.8881794 , 2.93103431, 2.97388923, 3.01674414,
            3.05959905, 3.10245397, 3.14530888, 3.18816379]), 
            
            array([3.18816379, 3.31316379, 3.43816379, 3.56316379, 3.68816379]), 
            
            array([3.68816379, 3.81316379, 3.93816379, 4.06316379, 4.18816379])]
    
    3. distances_from_gamma_lst
    ---------------------------
            [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.5621134962789892, 0.6242260981323974, 0.6863386999858055, 0.7484517490576391, 0.8105652453366283, 0.8726778471900365, 0.9155327607706284, 0.9583876743512203, 1.001242587931812, 1.0440975015124039, 1.0869524150929957, 1.1298073286735875, 1.1726622422541795, 1.2155171558347713, 1.2583720694153633, 1.301226982995955, 1.3440818965765469, 1.4690818965765469, 1.5940818965765469, 1.7190818965765469, 1.8440818965765469, 1.894081896576547, 1.944081896576547, 1.994081896576547, 2.044081896576547, 2.094081896576547, 2.1440818965765467, 2.1940818965765465, 2.2440818965765468, 2.2940818965765466, 2.3440818965765464, 2.4061953928555355, 2.4683079947089435, 2.5304205965623514, 2.5925336456341848, 2.654647141913174, 2.716759743766582, 2.7596146573471736, 2.8024695709277654, 2.845324484508357, 2.888179398088949, 2.9310343116695408, 2.9738892252501326, 3.0167441388307243, 3.059599052411316, 3.102453965991908, 3.1453088795724997, 3.1881637931530915, 3.1881637931530915, 3.3131637931530915, 3.4381637931530915, 3.5631637931530915, 3.6881637931530915, 3.6881637931530915, 3.8131637931530915, 3.9381637931530915, 4.063163793153091, 4.188163793153091]
    '''
    kpaths_distances_from_gamma_lst:List[np.ndarray] = []
    for tmp_idx_pair in cutoff_idxs_pair_lst:
        #print(tmp_idx_pair)
        tmp_distances_from_gamma_array = np.cumsum(distances_array[tmp_idx_pair[0]:tmp_idx_pair[1]], axis=0)
        kpaths_distances_from_gamma_lst.append( tmp_distances_from_gamma_array )
    #print([len(item) for item in kpaths_distances_from_gamma_lst])
    
    new_kpaths_distances_from_gamma_lst:List[np.ndarray] = []
    for idx_kpath, tmp_kpath_distance_from_gamma_array in enumerate(kpaths_distances_from_gamma_lst):
        if idx_kpath == 0:
            pass
        else:
            ### Note
            tmp_kpath_distance_from_gamma_array = tmp_kpath_distance_from_gamma_array - \
                                            tmp_kpath_distance_from_gamma_array[0] + \
                                            new_kpaths_distances_from_gamma_lst[idx_kpath-1][-1]
        new_kpaths_distances_from_gamma_lst.append(tmp_kpath_distance_from_gamma_array)
    num_kpts = sum([item.shape[0] for item in new_kpaths_distances_from_gamma_lst])
    assert(num_kpts == kpt_coords_array.shape[0])
    
    distances_from_gamma_lst:List[float] = [round(tmp_distance, 4) for tmp_array in new_kpaths_distances_from_gamma_lst for tmp_distance in list(tmp_array)]
    #print(new_kpaths_distances_from_gamma_lst)
    #print(distances_from_gamma_lst)
    
    ### Step 5. 得到高对称点的名称和对应横坐标
    '''
    1. hsp_names_lst
    ----------------
        - e.g. ['G', 'M', 'K', 'G', 'A', 'L', 'H', 'A', 'L', 'M', 'K', 'H']
    
    2. hsp_xvalues_lst
    ------------------
        - e.g. [0.0, 0.5, 0.8727, 1.3441, 1.8441, 2.3441, 2.7168, 3.1882, 3.1882, 3.6882, 3.6882, 4.1882]
    '''
    hsp_names_lst = []
    hsp_xvalues_lst = []
    for key, value in hsp_idx2name.items():
        hsp_names_lst.append(value)
        hsp_xvalues_lst.append(distances_from_gamma_lst[key])
    
    return distances_from_gamma_lst, hsp_names_lst, hsp_xvalues_lst
    
    
def get_dfs_bandstructure(file_path:str):
    '''
    Description
    -----------
        1. 得到每条 band 的横/纵坐标
            - 横坐标：|x_coordination| + |y_coordination| + |z_coordination|
            - 纵坐标：eigen energy for each eignstate
    
    Parameters
    ----------
        1. file_path: str
            - 此处特指 REPORT 文件
    
    Temp variables
    --------------
        1. num_kpt: int
            - kpoints 的数目
        2. num_band: int
            - 能带的数目 （每个kpoint处，本征态的数目）
        3. num_lines_for_band: int
            - 每个 Kpoint 的 eigen energies 占据几行
        4. kpts_coords_array: np.ndarray
            - 所有 kpoints 的坐标
        5. mark_ispin: bool
            - True: 打开自旋
            - False: 关闭自旋
        6. spin2eigen_energies
            - e.g. {"up":[], "down":[]}
            - spin2eigen_energies["up"] / spin2eigen_energies["down"]
                1. 一维：kpoints
                2. 二维：eigen energies
        
    Return
    ------
        1. spin2eigen_energies: Dict[]
            - e.g. {"up":[], "down":[]}
    '''
    ### Step 1. 从 REPORT 得到 `NUM_KPT` 和 `NUM_BAND`
    ### Step 1.1. 读取 `NUM_KPT`
    aim_content_kpt = "NUM_KPT"
    idx_row_kpt = search_aim(
                file_path=file_path,
                aim_content=aim_content_kpt)[0]
    num_kpt = int( linecache.getline(file_path, idx_row_kpt).split()[-1] )

    ### Step 1.2. 读取 `NUM_BAND`，并得到 `num_lines_for_plot`
    aim_content_band = "NUM_BAND"
    idx_row_band = search_aim(
                file_path=file_path,
                aim_content=aim_content_band)[0]
    num_band = int( linecache.getline(file_path, idx_row_band).split()[-1] )
    # `num_lines_for_band` 用于读取 eigen energies
    num_lines_for_band = math.ceil(num_band / NUM_PER_LINE)

    ### Step 1.3. 读取 kpoints 坐标
    aim_content_kpt_coords = "total number of K-point:"
    '''
    total number of K-point:          75
        0.00000     0.00000    0.00000     0.01333
        0.00000     0.02735    0.00000     0.01333
        0.00000     0.05470    0.00000     0.01333
    
    开始的行数 -- `idx_row_kpt_coords` (Note: 从 1 开始的!!!)
    '''
    kpts_coords_lst = []    # Kpoints 的坐标
    idx_row_kpt_coords = int( search_aim(
                file_path=file_path,
                aim_content=aim_content_kpt_coords)[0] )
    with open(file_path, "r") as f:
        lines_lst = f.readlines()
    for idx_row in range(
                    idx_row_kpt_coords,
                    idx_row_kpt_coords+num_kpt):
        tmp_row = lines_lst[idx_row]
        tmp_kpt_coord = tmp_row.split()
        kpts_coords_lst.append([float(value) for value in tmp_kpt_coord])
    
    kpts_coords_array = np.array(kpts_coords_lst)   # 用于生成能带图的横坐标

    ### Step 2. 读取 kpoints (横坐标) 和 eigen energies (纵坐标)
    ### Step 2.1. 横坐标: 从 IN.KPT 中读取
    #print(kpts_coords_array[:, :3])

    
    ### Step 2.2. 纵坐标
    spin2eigen_energies = {"up":[], "down":[]}
    aim_content_eigen = "eigen energies, in eV"
    idxs_eigen_start_lst = search_aim(
                                file_path=file_path,
                                aim_content=aim_content_eigen)
    
    for tmp_idx, tmp_idx_eigen_start in enumerate(idxs_eigen_start_lst):
        '''
        Parameters
        ----------
            1. tmp_idx: int
                - enumrate() 函数的输出。
            2. tmp_idx_eign_start: int
                - "eigen energies, in eV" 出现的行数
        
        Function
        --------
            eigen energies, in eV
                -62.852423       -62.852240       -62.852238       -62.834165       -37.088712
                -37.047212       -37.027703       -37.027568       -37.027541       -36.965955
                -36.965947       -36.965879       -36.929501       -36.886919       -36.886886
                -36.886435       -15.007332       -15.007171       -15.007095       -14.327065
                -14.326864       -14.326810       -13.948161       -13.865514        -7.353732
                -6.882147        -6.882129        -6.882113        -6.544601        -6.025924
                -5.798665        -5.798567        -5.798527        -5.632846        -5.632843
                -5.632839        -5.534179        -5.150396        -5.150379        -5.150363
                -4.845825        -4.134236        -3.952180        -3.952116        -3.952065
                -3.034926        -3.034914        -3.034805        -2.773082        -2.772978
                -2.772858        -2.012846        -0.342724        -0.061788        -0.061683
                -0.061631         0.461498         0.461835         0.461957         0.665682
                0.665901         0.665981         1.072153         1.539478
        ->
            [-62.852423, -62.85224, -62.852238, -62.834165, -37.088712, -37.047212, -37.027703, -37.027568, -37.027541, -36.965955, -36.965947, -36.965879, -36.929501, -36.886919, -36.886886, -36.886435, -15.007332, -15.007171, -15.007095, -14.327065, -14.326864, -14.32681, -13.948161, -13.865514, -7.353732, -6.882147, -6.882129, -6.882113, -6.544601, -6.025924, -5.798665, -5.798567, -5.798527, -5.632846, -5.632843, -5.632839, -5.534179, -5.150396, -5.150379, -5.150363, -4.845825, -4.134236, -3.95218, -3.952116, -3.952065, -3.034926, -3.034914, -3.034805, -2.773082, -2.772978, -2.772858, -2.012846, -0.342724, -0.061788, -0.061683, -0.061631, 0.461498, 0.461835, 0.461957, 0.665682, 0.665901, 0.665981, 1.072153, 1.539478]
        '''
        tmp_eigen_energies_ = lines_lst[tmp_idx_eigen_start:tmp_idx_eigen_start+num_lines_for_band]
        tmp_eigen_energies = [float(eigen) for tmp_5_eigen in tmp_eigen_energies_ for eigen in tmp_5_eigen.split()]
        
        if (tmp_idx < num_kpt):
            spin2eigen_energies["up"].append(tmp_eigen_energies)
        else:
            spin2eigen_energies["down"].append(tmp_eigen_energies)
    
    if not ( len(spin2eigen_energies["down"]) == 0 ):   ### 当自旋打开时，我们需要保证自旋向上、向下的 kpoints 数目相等
        assert ( len(spin2eigen_energies["up"]) == len(spin2eigen_energies["down"]) )
    
    return spin2eigen_energies


def plot_bands(
            xs_lst:List[float],
            yss_lst:List[pd.DataFrame],
            ):
    '''
    Parameters
    ----------
        1. xs_lst: List[float]
        2. ys_lst: List[pd.DataFrame]
    '''
    plt.figure(figsize=(10, 8))
    for df_eigen_energies in yss_lst:
        if not df_eigen_energies.empty: # "spindown" 的 pd.DataFrame 是否为空
            for idx_band in range(df_eigen_energies.shape[0]):  # df_eigen_energies.shape[0]: Number of kpoints
                #print(list( df_eigen_energies.loc[idx_band, :].to_numpy() ), len(xs_lst))
                plt.plot(
                        xs_lst, 
                        list( df_eigen_energies.loc[idx_band, :].to_numpy() ),
                        c="blue",
                        )
    #plt.xlim(-5, 5)
    plt.ylim(-5, 5)
                
    plt.savefig("/data/home/liuhanyu/hyliu/pwmat_demo/band/test.png")
    


def opt4():
    '''
    Description
    -----------
        1. 绘制能带
    '''
    current_path = os.getcwd()
    in_kpt_path = os.path.join(current_path, "IN.KPT")
    report_file_path = os.path.join(current_path, "REPORT")
    
    ### Step 1. 读取 IN.KPT，得到横坐标。高对称的名称和 xticknames
    distances_from_gamma_lst, hsp_names_lst, hsp_xvalues_lst = \
                            get_xaxis_from_inkpt(in_kpt_path=in_kpt_path, report_path=report_file_path)
    xs_lst = distances_from_gamma_lst
    #print( xs_lst )
    
    ### Step 2. 读取 REPORT，得到纵坐标。IN.KPT读取所有的本征能量
    spin2eigen_energies = get_dfs_bandstructure(file_path=report_file_path)
    yss_lst = [
            pd.DataFrame( np.array(spin2eigen_energies["up"]).transpose(), columns=None ), 
            pd.DataFrame( np.array(spin2eigen_energies["down"]).transpose(), columns=None ),
            ]
    #print( yss_lst )
    
    
    plot_bands(xs_lst=xs_lst, yss_lst=yss_lst)
    
    
if __name__ == "__main__":
    opt4()