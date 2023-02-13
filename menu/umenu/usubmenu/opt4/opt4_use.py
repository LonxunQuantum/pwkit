import os 
import math
import linecache

import numpy as np


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
        5. spin2eigen_energies_lst
            - e.g. {"up":[], "down":[]}
            - spin2eigen_energies_lst["up"] / spin2eigen_energies_lst["down"]
                1. 一维：kpoints
                2. 二维：eigen energies
        
    Return
    ------
        1. 
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
    ### Step 2.1. 横坐标
    print(kpts_coords_array[:, :3])
    
    ### Step 2.2. 纵坐标
    spin2eigen_energies_lst = {"up":[], "down":[]}
    aim_content_eigen = "eigen energies, in eV"
    idxs_eigen_start_lst = search_aim(
                                file_path=file_path,
                                aim_content=aim_content_eigen)    
    for tmp_idx_eigen_start in idxs_eigen_start_lst:
        '''
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
        spin2eigen_energies_lst["up"].append(tmp_eigen_energies)
    
    print(spin2eigen_energies_lst)


def opt4():
    '''
    Description
    -----------
        1. 绘制能带
    '''
    current_path = os.getcwd()
    report_file_path = os.path.join(current_path, "REPORT")
    get_dfs_bandstructure(file_path=report_file_path)
    

if __name__ == "__main__":
    opt4()