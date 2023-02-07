import os
from pflow.io.publicLayer.structure import DStructure


def opt6():
    '''
    Description
    -----------
        1. cell格式 -> atomc.config格式
    
    Variables
    ---------
        1. input_file_path
        2. output_file_path
    '''
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    
    # 若不存在 cif 文件，则需要手动指明cif格式文件的文件名
    input_file_name = "atom.cell"
    input_file_path = os.path.join(current_path, input_file_name)
    while ( not os.path.exists(os.path.join(current_path, input_file_name)) ):
        os.system('''        echo -e "\n\033[31m - 未搜索到名为 {0} 的结构文件，需要手动指定cell格式的文件名...\033[0m\n"'''.format(input_file_name))
        input_file_name = input(" cell格式的文件名\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
    
    # e.g. output_file_name = "atom.config"
    output_file_name = "atom.config"
    output_file_path = os.path.join(current_path, output_file_name)
        
    
    ### Step 2. 文件格式转换
    os.system("$PWKIT_ROOT/menu/scripts/cell2config.x < {0}".format(input_file_name))


    ### Step 3. 输出程序运行的信息
    print_sum(input_file_name, output_file_name)
    

def print_sum(input_file_name:str,
            output_file_name:str):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入文件:")
    print("\t\t{0}".format(input_file_name))
    print("\t* 输出文件:")
    print("\t\t{0}".format(output_file_name))
    
    
    print("*{0:-^68}*".format("---------"))

if __name__ == "__main__":
    opt6()