import os
import sys
import numpy as np
from pflow.io.publicLayer.structure import DStructure


def get_basis_vector(atom_config_name:str):
    '''
    Description
    -----------
        1. 查看晶胞的基矢间夹角

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
    basis_vector_array = structure.lattice.matrix
    print(basis_vector_array)
    
    ### Step 2. 输出信息
    # 1. 
    print("\n")
    print("*{0:-^72}*".format(" Output "))
    print("\t* 结构文件:")
    print("\t\t{0}".format(atom_config_name))
    
    # 2. 
    def gat_angle(array_1:np.array, array_2:np.array):
        cos_angle = np.dot(array_1, array_2) / ( np.linalg.norm(array_1) * np.linalg.norm(array_2) )
        angle_rad = np.arccos(cos_angle)
        angle_deg = np.degrees(angle_rad)
        return angle_deg
    print("\t* 晶胞的基矢间夹角:")
    
    print("\t\t{0:<15}{1:<15}{2:<15}".format("alpha", "beta", "gamma"))
    alpha_angle = gat_angle(array_1=basis_vector_array[0], array_2=basis_vector_array[1])
    beta_angle = gat_angle(array_1=basis_vector_array[1], array_2=basis_vector_array[2])
    gamma_angle = gat_angle(array_1=basis_vector_array[2], array_2=basis_vector_array[0])
    
    print("\t\t{0:<15}{1:<15}{2:<15}".format(
                                round(alpha_angle, 2),
                                round(beta_angle, 2),
                                round(gamma_angle, 2)
                                        )
        )


    print("\t* 晶胞的体积(单位:埃^3) :")
    print("\t\t{0:<10}{1:<15}".format("volume", structure.volume))
    
    
    # 3. 
    print("*{0:-^72}*".format("---------"))




if __name__ == "__main__":
    ### 接收 shell 命令行传来的参数
    atom_config_name = sys.argv[1]
    
    ### 输出信息
    get_basis_vector(atom_config_name=atom_config_name)