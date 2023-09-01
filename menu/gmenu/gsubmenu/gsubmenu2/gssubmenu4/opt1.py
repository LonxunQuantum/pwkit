import os
from matersdk.io.publicLayer.structure import DStructure


def opt_1():
    ### Step 1. 得到 atom.config 格式的文件名
    current_path = os.getcwd()
    atom_config_name = "atom.config"
    
    if ( not os.path.exists(os.path.join(current_path, atom_config_name)) ):
        print("当前文件夹下不存在 atom.config 文件!")
    while ( not os.path.exists(os.path.join(current_path, atom_config_name)) ):
        atom_config_name = input(" 请输入atom.config格式的文件名\n ------------>>\n")
        print("当前文件夹下不存在 atom.config 文件!")
        
    
    ### Step 2. 按照原子序数整理 (从小到大排列)
    structure = DStructure.from_file(
                        file_path=os.path.join(current_path, atom_config_name),
                        file_format="pwmat",
                        coords_are_cartesian=False
    )
    structure.reformat_elements()
    structure.to(
                output_file_path="atom.config_reformat",
                output_file_format="pwmat",
                include_magnetic_moments=True,
    )
    
    


if __name__ == "__main__":
    opt_1()