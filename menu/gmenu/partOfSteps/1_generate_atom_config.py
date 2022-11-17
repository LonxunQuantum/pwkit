#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import sys
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
    
    
    def generate_atom_config(self):
        input_file_format = sys.argv[1]
        input_file_path = sys.argv[2]
        output_file_format = "pwmat"
        output_file_path = "atom.config"
        
        
        structure = DStructure.from_file(
                            file_format=input_file_format,
                            file_path=input_file_path,
                            )
        
        structure.to(
                    output_file_format=output_file_format,
                    output_file_path=output_file_path,
                    )

if __name__ == "__main__":
    if sys.argv[1] == "structure_convert_warning":
        AtomConfigGenerator.structure_convert_warning()
    else:
        atom_config_generator = AtomConfigGenerator()
        atom_config_generator.generate_atom_config()