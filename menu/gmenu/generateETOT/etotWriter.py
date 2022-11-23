#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os 
import sys

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
    "H3": "HSE03",
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
                etot_path:str=os.path.join(os.getcwd(), "etot.input"),
                atom_config_path:str=os.path.join(os.getcwd(), "atom.config")
                ):
        self.etot_path = etot_path
        self.atom_config_path = atom_config_path
        
        #if os.path.exists(self.etot_path):
        #    os.remove(self.etot_path)
    
    
    def write_task(self):
        '''
        Description
        -----------
            1. run in `1_write_task.py` file
        '''
        setattr(self, "task_name", sys.argv[1])
        
        with open(self.etot_path, "a") as f:
            f.write("### 并行设置: 波函数并行设置、K点并行设置，两者之积必须等于GPU总数\n")
            f.write("1  4\n\n")
            f.write("### 基础设置\n")
            f.write("JOB = {0}\n".format(task_short2name[self.task_name]))
    
    
    def write_functional(self):
        '''
        Description
        -----------
            1. run in `2_write_functional.py` file
        '''
        setattr(self, "functional_name", sys.argv[1])
        
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
    
    
    def write_accuracy(self):
        '''
        Description
        -----------
            1. run in `3_write_accuracy.py` file
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
                density = float(sys.argv[1])
                
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
    
    
    def write_scf(self):
        '''
        Description
        -----------
            1. run in `4_write_scf.py` file
        '''
        # density of KMesh (unit: 2pi/Angstrom)
        mp_n123 = None
        try:
            density = float(sys.argv[1])
            
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
            scf_iter0_1 = "6 4 3 0.0 0.0025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
            scf_iter1_1 = None

        if self.task_name == "CR":
            ecut = 70
            scf_iter0_1 = "6 4 3 0.0 0.0025 1"
            scf_iter0_2 = "94 4 3 1.0 0.025 1"
            scf_iter1_1 = "40 4 3 1.0 0.025 1"
        
        if self.task_name == "AR":
            ecut = 50
            scf_iter0_1 = "6 4 3 0.0 0.0025 1"
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
            1. run in `5_write_specific.py` file
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
                charge_capacity = sys.argv[2]
                #num_electron = num_electron_pseudo - charge_capacity
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
            
            
            # 8. 溶剂效应
            # etot.input输入输出设置添加
            #       IN.SOLVENT = T
            #       OUT.SOLVENT_CHARGE = T
            #       额外需要输出文件 IN.SOLVENT
            
            
    
    
    def write_input_output(self):
        '''
        Description
        -----------
            1. run in `6_write_input_output.py` file    
    
        Note
        ---- 
            1. 内部包含写入赝势文件 `IN.PSP1`, `IN.PSP2`, ...
        '''
        ### Part I. 根据赝势类型确定赝势文件后缀
        pseudo_name = sys.argv[1]
        # 1. SG15
        if pseudo_name == "SG":
            pseudo_suffix = ".SG15.PBE.UPF"
        # 2. PD04
        if pseudo_name == "PD":
            pseudo_suffix = None
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
            f.write("IN.ATOM = atom.config\n")
            
            ## Note: 赝势部分
            dstructure = DStructure.from_file(
                                file_format="pwmat",
                                file_path=self.atom_config_path,
                                )
            species_lst = [specie.symbol for specie in dstructure.species]
            species_lst = list(set(species_lst))
            for idx, element in enumerate(species_lst):
                f.write("IN.PSP{0} = {1}{2}\n".format(idx+1, element, pseudo_suffix))
            
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
                if (self.specific_name == "SE"):
                    f.write("IN.SOLVENT = T     # 溶剂效应\n")
                    f.write("OUT.SOLVENT_CHARGE = T     # 溶剂效应\n")
            except AttributeError:
                pass
    
    def write_pseudo(self):
        pass