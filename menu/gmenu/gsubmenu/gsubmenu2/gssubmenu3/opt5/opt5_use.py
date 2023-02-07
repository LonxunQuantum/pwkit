import os
import sys
from pflow.io.publicLayer.structure import DStructure


def get_basis_vector(atom_config_name:str):
    '''
    Description
    -----------
        1. 查看晶胞的基矢长度

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
    reciprocal_basis_vector_length_tuple = structure.lattice.reciprocal_lattice.abc
    
    ### Step 2. 输出信息
    # 1. 
    print("\n")
    print("*{0:-^72}*".format(" Output "))
    print("\t* 结构文件:", end="")
    print("\t\t{0}".format(atom_config_name))
    
    # 2. 
    print("\t* 倒易点阵的基矢长度(单位:2pi/埃) :")
    print("\t\t{0:<15}{1:<15}{2:<15}".format("b1-length", "b2-length", "b3-length"))
    print("\t\t{0:<15}{1:<15}{2:<15}".format(
                                        round(reciprocal_basis_vector_length_tuple[0], 4),
                                        round(reciprocal_basis_vector_length_tuple[1], 4),
                                        round(reciprocal_basis_vector_length_tuple[2], 4)
                                        )
        )
    
    
    # 3. 
    print("*{0:-^72}*".format("---------"))


if __name__ == "__main__":
    ### 接收 shell 命令行传来的参数
    atom_config_name = sys.argv[1]
    
    ### 输出信息
    get_basis_vector(atom_config_name=atom_config_name)