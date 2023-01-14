import os
import sys
import numpy as np
from pflow.io.publicLayer.structure import DStructure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


def get_symmetry_info(atom_config_name:str):
    '''
    Description
    -----------
        1. 查看晶胞的对称性信息

    Parameters
    ----------
        1. atom_config_name: str
            atom.config 格式的文件名
    '''
    current_path = os.getcwd()
    
    ### Step 1. 得到晶体相关信息
    atom_config_path = os.path.join(current_path, atom_config_name)
    structure = DStructure.from_file(
                            file_format="pwmat",
                            file_path=atom_config_path,
                            )
    
    ### Step 2. 输出信息
    ## 1. 
    print("\n")
    print("*{0:-^72}*".format(" Output "))
    print("\t* {0:<16} {1:<20}".format("结构文件:", atom_config_name))
    
    ## 2. 
    space_group_analyzer = SpacegroupAnalyzer(
                                    structure,
                                    symprec=1E-4,
                                    angle_tolerance=5.0)
    # 1). 晶系
    print("\t* {0:<20} {1:<20}".format(
                                "Crystal System:",
                                space_group_analyzer.get_crystal_system()
                                )
        )
    # 2). 空间群
    print("\t* {0:<20} ".format(
                                "Space Group:",
                                ),
        end=""
        )
    print(space_group_analyzer.get_space_group_operations())
    # 3). 点群
    print("\t* {0:<20} {1:<20}".format(
                                "Crystal Class:",
                                space_group_analyzer.get_point_group_symbol()
                                )
        )
    # 4) 对称操作个数
    print("\t* {0:<20} {1:<20}".format(
                                "Symmetry Operations:",
                                len(space_group_analyzer.get_symmetry_operations())
                                )
        )
    # 5) 精度
    print("\t* {0:<20} {1:<E}".format(
                                "Symmetry Accuracy:",
                                1E-4
                                )
    ) 
    #print(space_group_analyzer.get_symmetry_dataset())
    
    ## 3. 
    print("*{0:-^72}*".format("---------"))




if __name__ == "__main__":
    ### 接收 shell 命令行传来的参数
    atom_config_name = sys.argv[1]
    
    ### 输出信息
    get_symmetry_info(atom_config_name=atom_config_name)