#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import os 
import sys
import shutil
import numpy as np

from pflow.io.publicLayer.structure import DStructure
from pflow.calculation.kpoints.kmesh import KMesh


# `任务类型` 简写: PWmat任务类型
task_short2name = {
    "SC": "SCF",
    "CR": "RELAX",
    "AR": "RELAX",
    "NS": "NONSCF",
    "DS": "DOS",
    "OS": None,
    "EP": None,
    "MD": None,
    "NA": None,
    "TD": None, 
    "TC": None,
    "TS": None,
}
# `泛函设置` 简写: PWmat泛函类型
functional_short2name = {
    "PE": "PBE",
    "91": "PW91",
    "PS": "PBESOL",
    "LD": "LDA",
    "H6": "HSE",
    "H3": "HSE",
    "P0": "HSE",
    "B3": "XC_HYB_GGA_XC_B3LYP",
    "TP": "TPSS",
    "SC": "SCAN",
}

# `赝势设置` 简写: PWmat赝势类型
pseudo_short2name = {
    "SG": "SG15",
    "PD": "PD04",
    "FH": "FHI",
    "PW": "PWM",
    "UD": "自定义",
}

# `特殊设置` 简写: PWmat特殊设置



class EtotWriter(object):
    '''
    Description
    -----------
        1. `EtotWriter` 是一个 `BaseClass`，我们将在其他文件中调用
            这个类，逐行写入 `etot.input`
    
    Attributions
    ------------
        1. `self.write_task()`: 写入 `任务类型`
        2. `self.write_functional()`: 写入 `泛函设置`
        3. `self.write_pseudo()`: 写入 `赝势设置`
        4. `self.write_specific()`: 写入 `特殊设置`
    '''
    def __init__(self,
                atom_config_name:str,
                ):
        '''
        Parameters
        ----------
            1. atom_config_name: str
                具有 atom_config 格式的文件的名字
                -e.g. atom.pwamt, final.config, ...
        '''
        self.etot_path = os.path.join(os.getcwd(), "etot.input")
        self.atom_config_path = os.path.join(os.getcwd(), atom_config_name)
        
        # 特殊设置选择 `溶剂效应` 和 `固定电势` 的时候需要生成此文件
        self.in_solvent_path = os.path.join(os.getcwd(), "IN.SOLVENT")
        #if os.path.exists(self.etot_path):
        #    os.remove(self.etot_path)
    
    
    def write_task(self, task_name:str):
        '''
        Description
        -----------
            1. run in `1_write_task.py` file
        '''
        setattr(self, "task_name", task_name)
        
        with open(self.etot_path, "a") as f:
            f.write("1  4   # 并行设置: 波函数并行设置、K点并行设置，两者之积必须等于GPU总数\n\n")
            f.write("### 基础设置\n")
            f.write("JOB = {0}\n".format(task_short2name[self.task_name]))
    
    
    def write_functional(self, functional_name:str):
        '''
        Description
        -----------
            1. run in `2_write_functional.py` file
        '''
        setattr(self, "functional_name", functional_name)
        
        # 1. self.functional_name == H6
        if self.functional_name == "H6":
            hse_alpha = 0.25
            hse_beta = 0.0
            hse_omega = 0.2
        
        # 2. self.functional_name == H3
        if self.functional_name == "H3":
            hse_alpha = 0.25
            hse_beta = 0.0
            hse_omega = 0.3
        # 3. self.functional_name == P0
        if self.functional_name == "P0":
            hse_alpha = 0.25
            hse_beta = 0.0
            hse_omega = 0.0
        
        with open(self.etot_path, "a") as f:
            f.write("XCFUNCTIONAL = {0}\n".format(functional_short2name[self.functional_name]))

            if self.functional_name in ["H6", "H3", "P0"]:
                if ( self.functional_name == "H6" ):
                    note_hse = "HSE06"
                if ( self.functional_name == "H3" ):
                    note_hse = "HSE03"
                if ( self.functional_name ==  "P0"):
                    note_hse = "PBE0"
                    
                f.write("HSE_ALPHA = {0}    # {1}\n".format(
                                            hse_alpha, 
                                            note_hse,
                                            )
                        )
                f.write("HSE_BETA = {0}     # {1}\n".format(
                                            hse_beta, 
                                            note_hse,
                                            )
                        )
                f.write("HSE_OMEGA = {0}    # {1}\n".format(
                                            hse_omega, 
                                            note_hse,
                                            )
                        )
    
    
    def write_accuracy(self, density:float):
        '''
        Description
        -----------
            1. run in `3_write_accuracy.py` file
        
        Parameters
        ----------
            1. density: float
                K-Mesh density in 2pi/A.
        '''
        if self.task_name == "SC":
            accuracy = "NORMAL"
            convergence = "EASY"
            precision = "AUTO"
            
        if self.task_name == "CR":
            accuracy = "HIGH"
            convergence = "EASY"
            precision = "AUTO"
            
        if self.task_name == "AR":
            accuracy = "HIGH"
            convergence = "EASY"
            precision = "AUTO"
        
        if self.task_name == "NS":
            accuracy = "NORMAL"
            convergence = "EASY"
            precision = "AUTO"
        
        if self.task_name == "DS":
            # DOS_DETAIL
            dos_gaussian_broadening = "0.05"
            num_dos_grid = 4000
            accuracy = "NORMAL"
            convergence = "EASY"
            precision = "AUTO"
            
            # DOS_DETAIL      
            try:
                density = density
                
                kmesh = KMesh(file_format="pwmat",
                            file_path=self.atom_config_path
                            )
                kmesh_lst = list(kmesh.get_kmesh(density=density))
                kmesh_lst = [str(int(value)) for value in kmesh_lst]
                kmesh_str = " ".join(kmesh_lst)
                
                dos_detail = "0 {0}".format(kmesh_str)
            except:
                pass
        
        with open(self.etot_path, "a") as f:
            # self.task_name == DS : dos writing
            if self.task_name == "DS":
                f.write("DOS_DETAIL = {0}\n".format(dos_detail))
                f.write("DOS_GAUSSIAN_BROADENING = {0}\n".format(dos_gaussian_broadening))
                f.write("NUM_DOS_GRID = {0}\n".format(num_dos_grid))
            
            
            # common writing
            f.write("ACCURACY = {0}\n".format(accuracy))
            f.write("CONVERGENCE = {0}\n".format(convergence))
            f.write("PRECISION = {0}\n".format(precision))
    
    
    def write_scf(self, density:float):
        '''
        Description
        -----------
            1. run in `4_write_scf.py` file
            
        Parameters
        ----------
            1. density: float
                K-Mesh density in 2pi/A
        '''
        # density of KMesh (unit: 2pi/Angstrom)
        mp_n123 = None
        try:
            density = density
            
            kmesh = KMesh(file_format="pwmat",
                          file_path=self.atom_config_path
                        )
            kmesh_lst = list(kmesh.get_kmesh(density=density))
            kmesh_lst = [str(int(value)) for value in kmesh_lst]
            kmesh_str = " ".join(kmesh_lst)
            
            mp_n123 = "{0} 0 0 0 0".format(kmesh_str)
        except:
            pass
            
            
        if self.task_name == "SC":
            ecut = 50
            # mp_n123 = mp_n123
            scf_iter0_1 = "6 4 3 0.0 0.025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
            scf_iter1_1 = None

        if self.task_name == "CR":
            ecut = 70
            scf_iter0_1 = "6 4 3 0.0 0.025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
            scf_iter1_1 = "40 4 3 1.0 0.025 1"
        
        if self.task_name == "AR":
            ecut = 50
            scf_iter0_1 = "6 4 3 0.0 0.025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
            scf_iter1_1 = "40 4 3 1.0 0.025 1"
        
        if self.task_name == "NS":
            ecut = 50
            scf_iter0_1 = "50 4 3 0.0 0.025 1"
            scf_iter0_2 = None
            scf_iter1_1 = None
        
        if self.task_name == "DS":
            ecut = 50
            scf_iter0_1 = None
            scf_iter0_2 = None
            scf_iter1_1 = None
        
        with open(self.etot_path, "a") as f:
            f.write("\n\n")
            f.write("### 电子自洽设置\n")
            f.write("Ecut = {0}\n".format(ecut))
            if mp_n123:
                f.write("MP_N123 = {0}\n".format(mp_n123))
            if scf_iter0_1:
                f.write("SCF_ITER0_1 = {0}\n".format(scf_iter0_1))
            if scf_iter0_2:
                f.write("SCF_ITER0_2 = {0}\n".format(scf_iter0_2))
            if scf_iter1_1:
                f.write("SCF_ITER1_1 = {0}\n".format(scf_iter1_1))
    
    
    
    
    def write_specific(self):
        '''
        Description
        -----------
            1. run in `6_write_specific.py` file
        
        Note
        ----
            1. 选择`溶剂效应`和`固定电势`的时候，需要添加 `IN.SOLVENT` 文件
        '''
        setattr(self, "specific_name", sys.argv[1])
        
        # 首次写入 "#特殊设置\n" 
        mark_first = False
        with open(self.etot_path, "r") as f:
            rows_content = f.readlines()
            if "### 特殊设置\n" not in rows_content:
                mark_first = True
        
        # 写入 PWmat 的选项
        with open(self.etot_path, "a") as f:
            if mark_first == True:
                f.write("\n\n")
                f.write("### 特殊设置\n")           
            # 1. 自旋极化
            if (self.specific_name == "SP"):
                f.write("SPIN = 2   # 自旋极化\n")
            # 2. 自旋轨道耦合
            if (self.specific_name == "SO"):
                f.write("SPIN = 22  # 自旋轨道耦合\n")
            # 3. 非共线磁矩+自旋轨道耦合
            if (self.specific_name == "SN"):
                f.write("SPIN = 222 # 非共线磁矩+自旋轨道耦合\n")
            # 4. 带电体系
            if (self.specific_name == "CS"):
                charge_capacity = float(sys.argv[2])
                sg15_dir_path = sys.argv[3]
                
                # 4.1. 从 `赝势SG15` 中得到体系的 `中性电子数`
                num_electron_pseudo = 0
                dstructure = DStructure.from_file(
                                file_format="pwmat",
                                file_path=self.atom_config_path,
                                )
                species_lst = [specie.symbol for specie in dstructure.species]
                species_lst = list(set(species_lst))
                
                specie2valence = {} # 键：元素种类； 值：价电子数
                for tmp_specie in species_lst:  # 循环得到 tmp_specie 的价电子数
                    element_sg15_path = os.path.join(sg15_dir_path, "{0}.SG15.PBE.UPF".format(tmp_specie))
                    with open(element_sg15_path, "r") as f_pseudo:
                        content = f_pseudo.readlines()
                    for row in content:
                        if "z_valence" in row:
                            valence_tmp_specie = float( row.split('"')[-2] )
                    specie2valence.update({tmp_specie: valence_tmp_specie})
                
                specie2num = {} # 键：元素种类； 值：元素原子的数目
                for tmp_specie in species_lst:  # 循环得到 tmp_specie 的原子数目
                    num_tmp_specie = species_lst.count(tmp_specie)
                    specie2num.update({tmp_specie: num_tmp_specie})
                    
                for tmp_specie in species_lst:
                    num_electron_pseudo += specie2num[tmp_specie] * specie2valence[tmp_specie]

                # 4.2. 电子数计算公式：num_electron = num_electron_pseudo - charge_capacity
                num_electron = num_electron_pseudo - charge_capacity
                # 保留三位小数
                num_electron = round(num_electron, 3)
                
                f.write("NUM_ELECTRON = {0} # 带电体系: 电子数=中性电子数(通过赝势计算所得)-带电量\n".format(num_electron))
            
            # 5. DFT+U
            if (self.specific_name == "PU"):
                dstructure = DStructure.from_file(
                                    file_format="pwmat",
                                    file_path=self.atom_config_path,
                                    )
                species_lst = [specie.symbol for specie in dstructure.species]
                species_lst = list(set(species_lst))
                for idx, element in enumerate(species_lst):
                    f.write("LDAU_PSP{0} = -1 0.0   # DFT+U\n".format(idx+1))
            
            # 6. DFT+D3
            if (self.specific_name == "D3"):
                f.write("VDW = DFT-D3   # DFT-D3修正\n")
            
            # 7. 固定电势计算
            # etot.input输入输出设置添加
            #       IN.SOLVENT = T
            #       OUT.SOLVENT_CHARGE = T
            #       额外需要输出文件 IN.SOLVENT
            if (self.specific_name == "FF"):
                electrode_potential = float( sys.argv[2] )
                # Ef计算公式: Ef = -4.42 - 电极电势值
                e_f = -4.42 - electrode_potential
                # 保留两位小数
                e_f = round(e_f, 2)
                f.write("FIX_FERMI = {0}  0.1  0.06 # 固定电势计算\n".format(e_f))

                # 7.1. 编写 IN.SOLVENT 文件
                dstructure = DStructure.from_file(
                        file_format="pwmat",
                        file_path=self.atom_config_path,
                        )
                species_lst = [specie.symbol for specie in dstructure.species]
                species_lst = list(set(species_lst))
                num_species = len(species_lst)
                with open(self.in_solvent_path, "a") as f_in_solvent:
                    for idx_specie in range(num_species):
                        f_in_solvent.write("PARAM_CHARGE.{0} = 1 1 1 #内容均为1 1 1。有{1}种元素，就是{2}行，这里是第{3}个元素\n".format(idx_specie+1, num_species, num_species, idx_specie+1))
                    f_in_solvent.write("DIELECTRIC_MODEL = ATOM_CHARGE\n")
                    f_in_solvent.write("DIELECTRIC_CONST = 78\n")
                    f_in_solvent.write("RHOMIN_DIELECTRIC = 0.0001\n")
                    f_in_solvent.write("RHOMAX_DIELECTRIC = 0.005\n")
                    f_in_solvent.write("SURFACE_TENSION = 50\n")
                    f_in_solvent.write("PRESSURE = -0.35\n")
                    f_in_solvent.write("RHOMAX_CAVITY = 0.005\n")
                    f_in_solvent.write("RHOMIN_CAVITY = 0.0001\n")
                    f_in_solvent.write("POISSON_BOLTZMANN = T\n")
                    f_in_solvent.write("AKK0_DEBY = 0.036\n")
                    f_in_solvent.write("RHOMIN_DEBY = 0.0001\n")
                    f_in_solvent.write("RHOMAX_DEBY = 0.005\n")
            
            # 8. 溶剂效应
            # etot.input输入输出设置添加
            #       IN.SOLVENT = T
            #       OUT.SOLVENT_CHARGE = T
            #       额外需要输出文件 IN.SOLVENT
            if (self.specific_name == "SE"):
                # 8.1. 编写 IN.SOLVENT 文件
                dstructure = DStructure.from_file(
                        file_format="pwmat",
                        file_path=self.atom_config_path,
                        )
                species_lst = [specie.symbol for specie in dstructure.species]
                species_lst = list(set(species_lst))
                num_species = len(species_lst)
                with open(self.in_solvent_path, "a") as f_in_solvent:
                    for idx_specie in range(num_species):
                        f_in_solvent.write("PARAM_CHARGE.{0} = 1 1 1 #内容均为1 1 1。有{1}种元素，就是{2}行，这里是第{3}个元素\n".format(idx_specie+1, num_species, num_species, idx_specie+1))
                    f_in_solvent.write("DIELECTRIC_MODEL = ATOM_CHARGE\n")
                    f_in_solvent.write("DIELECTRIC_CONST = 78\n")
                    f_in_solvent.write("RHOMIN_DIELECTRIC = 0.0001\n")
                    f_in_solvent.write("RHOMAX_DIELECTRIC = 0.005\n")
                    f_in_solvent.write("SURFACE_TENSION = 50\n")
                    f_in_solvent.write("PRESSURE = -0.35\n")
                    f_in_solvent.write("RHOMAX_CAVITY = 0.005\n")
                    f_in_solvent.write("RHOMIN_CAVITY = 0.0001\n")
                    f_in_solvent.write("POISSON_BOLTZMANN = F\n")
                    f_in_solvent.write("AKK0_DEBY = 0.036\n")
                    f_in_solvent.write("RHOMIN_DEBY = 0.0001\n")
                    f_in_solvent.write("RHOMAX_DEBY = 0.005\n")
                
            
    
    
    def write_input_output(self,
                        pseudo_name:str,
                        atom_config_format_file_name:str,
                        pseudo_dir_path:str,
                        ):
        '''
        Description
        -----------
            1. run in `6_write_input_output.py` file    
    
        Note
        ---- 
            1. 内部包含写入赝势文件 `IN.PSP1`, `IN.PSP2`, ...
        '''
        ### Part I. 根据赝势类型确定赝势文件后缀、赝势所在的文件夹路径
        pseudo_name = pseudo_name
        pseudo_dir_path = pseudo_dir_path
        # 1. SG15
        if pseudo_name == "SG":
            pseudo_suffix = ".SG15.PBE.UPF"
        # 2. PD04
        if pseudo_name == "PD":
            pseudo_suffix = ".PD04.PBE.UPF"
        # 3. FHI
        if pseudo_name == "FH":
            pseudo_suffix = None
        # 4. PWM
        if pseudo_name == "PW":
            pseudo_suffix = None
        # 5. 自定义
        if pseudo_name == "UD":
            pseudo_suffix = None
        
        
        ### Part II. 根据任务类型写入 `etot.input`
        # 1. task_name == SC        
        if self.task_name == "SC":
            in_wg = "F"
            in_rho = "F"
            in_vr = "F"
            in_kpt = "F"
            out_wg = "T"
            out_rho = "T"
            out_vr = "T"
            out_vatom = "T"
        
        # 2. task_name == CR
        if self.task_name == "CR":
            in_wg = "F"
            in_rho = "F"
            in_vr = "F"
            in_kpt = "F"
            out_wg = "T"
            out_rho = "T"
            out_vr = "T"
            out_vatom = "F"
            
        # 3. task_name = AR
        if self.task_name == "AR":
            in_wg = "F"
            in_rho = "F"
            in_vr = "F"
            in_kpt = "F"
            out_wg = "T"
            out_rho = "T"
            out_vr = "T"
            out_vatom = "F"
            
        # 4. task_name == NS
        if self.task_name == "NS":
            in_wg = "F"
            in_rho = "F"
            in_vr = "T"
            in_kpt = "T"
            out_wg = "T"
            out_rho = "F"
            out_vr = "F"
            out_vatom = "F"

        # 5. task_name == DS
        if self.task_name == "DS":
            in_wg = "T"
            in_rho = "F"
            in_vr = "F"
            in_kpt = "F"
            out_wg = "F"
            out_rho = "F"
            out_vr = "F"
            out_vatom = "F"
            
        with open(self.etot_path, "a") as f:
            f.write("\n\n")
            f.write("### 输入输出设置\n")
            f.write("IN.ATOM = {0}\n".format(atom_config_format_file_name))
            
            ## Note: 赝势部分
            dstructure = DStructure.from_file(
                                file_format="pwmat",
                                file_path=self.atom_config_path,
                                )
            species_lst = [specie.symbol for specie in dstructure.species]
            species_lst = list(set(species_lst))
            for idx, element in enumerate(species_lst):
                f.write("IN.PSP{0} = {1}{2}\n".format(idx+1, element, pseudo_suffix))
                
                # 把对应的赝势文件拷贝到当前工作目录
                pseudo_name = "{0}{1}".format(element, pseudo_suffix)
                src_path = os.path.join(pseudo_dir_path, pseudo_name)
                dst_path = os.path.join(os.getcwd(), pseudo_name)
                shutil.copy(src=src_path, dst=dst_path)
            
            f.write("IN.WG = {0}\n".format(in_wg))
            f.write("IN.RHO = {0}\n".format(in_rho))
            f.write("IN.VR = {0}\n".format(in_vr))
            f.write("IN.KPT = {0}\n".format(in_kpt))
            f.write("OUT.WG = {0}\n".format(out_wg))
            f.write("OUT.RHO = {0}\n".format(out_rho))
            f.write("OUT.VR = {0}\n".format(out_vr))
            f.write("OUT.VATOM = {0}\n".format(out_vatom))
            
            
            ### 某些 `特殊设置` 需要添加输入输出
            try:    # 当没有 `特殊设置` 时，没有 `self.specific_name` 属性
                # 1. `特殊设置` == 溶剂效应
                if (self.specific_name == "SE"):
                    f.write("IN.SOLVENT = T     # 溶剂效应\n")
                    f.write("OUT.SOLVENT_CHARGE = T     # 溶剂效应\n")
                # 2. `特殊设置` == 固定电势
                if (self.specific_name == "FF"):
                    f.write("IN.SOLVENT = T     # 固定电势计算\n")
                    f.write("OUT.SOLVENT_CHARGE = T     # 固定电势计算\n")    
            except AttributeError:
                pass
    
    
    
    def write_other(self):
        '''
        Description
        -----------
            1. Run in `6_write_input_output.py` file 
        '''
        dstructure = DStructure.from_file(
                                file_format="pwmat",
                                file_path=self.atom_config_path,
                                )
        
        # 1. 判断是否需要添加偶极矩修正: 真空>8，添加偶极修正
        dipole_moment_mark = False
        z_coordination_min = np.min(dstructure.cart_coords[:, 2])
        z_coordination_max = np.max(dstructure.cart_coords[:, 2])
        z_coordination_space = z_coordination_max - z_coordination_min
        lattice_z_space = dstructure.lattice.matrix[2, 2]
        if ( (lattice_z_space - z_coordination_space) > 8):
            dipole_moment_mark = True
        
        # 2. 偶极矩修正: 计算 X3
        edge_x3 = round( np.mean(dstructure.frac_coords[:, 2]) - 0.5, 3)
        if (edge_x3 < 0):
            edge_x3 = 1 + edge_x3
        
        with open(self.etot_path, "a") as f:
            f.write("\n\n")
            f.write("### 其他设置\n")
            if dipole_moment_mark:
                f.write("#COULOMB = 13  {0}  # 偶极矩修正\n".format(edge_x3))
            f.write("#CHARGE_DECOMP = T\n")
            f.write("#NUM_BAND = XX\n")
            f.write("#SYMM_PREC = 1E-5\n")
    
    
    
    def write_pseudo(self):
        pass