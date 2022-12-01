import os
import sys
import linecache
from pflow.io.publicLayer.structure import DStructure


class AtomConfigGenerator(object):
    def __init__(self):
        pass
    
    
    @staticmethod
    def structure_convert_warning():
        print("+{0:-^58}+".format("Warm Tips"))
        print("\t* 结构文件的格式:")
        print("\t\t1.pwmat  2.vasp  3.mcsqs  4.json")
        print("\t\t5.xsf    6.yaml  7.cssr   8.prismatic")
        print("+{0:-^58}+".format("---------"))
        
        
    @staticmethod
    def judge_atom_config_exist():
        '''
        Description
        -----------
            1. 判断当前文件夹下是否存在 atom.config 格式的文件
                1.1. 第二行有 "Lattice"     (大小写无所谓)
                1.2. 第二行有 "vector"      (大小写无所谓)
                1.3. 第三行有 "Position"    (大小写无所谓)
        
        Return
        ------
            1. exist_mark: bool
                - True: 存在
                - False: 不存在
        '''
        # atom.config 格式的文件名
        atom_config_name = None
        
        current_dir_path = os.getcwd()
        for tmp_file_name in os.listdir(current_dir_path):
            try:
                tmp_file_path = os.path.join(current_dir_path, tmp_file_name)
                
                if not os.path.isfile(tmp_file_path):
                    # 1. 不处理 文件夹
                    continue
                
                if "UPF" in tmp_file_name:
                    # 2. 不处理 赝势文件
                    continue
                
                if (tmp_file_name == "etot.input"):
                    # 3. 不处理 etot.input
                    continue
                
                if (tmp_file_name == "etot_writer.pkl"):
                    # 4. 不处理 etot_writer.pkl
                    continue
                
                if "OUT" in tmp_file_name:
                    # 5. 不处理带 OUT 的文件
                    continue
                
                if "REPORT" in tmp_file_name:
                    # 6. 不处理带 REPORT 的文件
                    continue
                
                if "slurm" in tmp_file_name:
                    # 7. 不处理 slurm 集群的输出文件
                    continue

                # 将 第2行 和 第6行 的所有字符串变成大写形式
                # tmp_rows_lst[1].split(): ['Lattice', 'vector']
                # tmp_rows_lst[5].split(): ['Position,', 'move_x,', 'move_y,', 'move_z']
                tmp_rows_lst_1_upper = [string.upper() for string in linecache.getline(tmp_file_path, 2).split()]
                tmp_rows_lst_5_upper = [string.upper().replace(',','') for string in linecache.getline(tmp_file_path, 6).split()]
                # tmp_rows_lst_1_upper: ['LATTICE', 'VECTOR']
                # tmp_rows_lst_5_upper: ['POSITION,', 'MOVE_X,', 'MOVE_Y,', 'MOVE_Z']
                if ("LATTICE" in tmp_rows_lst_1_upper and \
                    "VECTOR" in tmp_rows_lst_1_upper and \
                    "POSITION" in tmp_rows_lst_5_upper
                    ):
                    atom_config_name = tmp_file_name
                    
            except:
                pass
        
        
        # return to shell
        print(atom_config_name)
    
    
    def generate_atom_config(self,
                            input_file_format,
                            input_file_path,
                            ):
        '''
        Description
        -----------
            1. 如果没有 atom.config 格式的结构文件，则需要转换当前结构文件的路径。
        '''
        input_file_format = input_file_format
        input_file_path = input_file_path
        output_file_format = "pwmat"
        output_file_path = "atom.config"
        
        try:
            structure = DStructure.from_file(
                                file_format=input_file_format,
                                file_path=input_file_path,
                                )
            structure.to(
                        output_file_format=output_file_format,
                        output_file_path=output_file_path,
                        )
        except:
            print("Check_structure_file")
        

if __name__ == "__main__":
    if sys.argv[1] == "judge_atom_config_exist":
        AtomConfigGenerator.judge_atom_config_exist()
        
    elif sys.argv[1] == "structure_convert_warning":
        AtomConfigGenerator.structure_convert_warning()
        
    else:
        atom_config_generator = AtomConfigGenerator()
        atom_config_generator.generate_atom_config(
                                input_file_format=sys.argv[1],
                                input_file_path=sys.argv[2],
                                )