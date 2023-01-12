import os
from pflow.io.publicLayer.structure import DStructure


def opt2():
    '''
    Description
    -----------
        1. xsf格式 -> atomc.config格式
    
    Variables
    ---------
        1. input_file_path
        2. output_file_path
    '''    
    mark_xsf_exits = False
    
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    for file_name in os.listdir(current_path):
        file_path = os.path.join(current_path, file_name)
        # 默认输入 atom.xsf 文件，进行格式转换        
        if os.path.isfile(file_path) and (file_name=="xatom.xsf"):
            input_file_name = "xatom.xsf"
            input_file_path = file_path
            mark_xsf_exits = True
            break
    
    # 若不存在 xsf 文件，则需要手动指明xsf格式文件的文件名
    if mark_xsf_exits == False:
        os.system('''        echo -e "\n\033[31m - 未搜索到名为xatom.xsf的结构文件，需要手动指定xsf格式的文件名...\033[0m\n"''')
        input_file_name = input(" xsf格式的文件名\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
    
    # e.g. output_file_name = "xsf_prefix.atom.config"
    output_file_name = "{0}.atom.config".format( input_file_name.split('.')[0] )
    output_file_path = os.path.join(current_path, output_file_name)
        
    
    ### Step 2. 文件格式转换
    structure = DStructure.from_file(file_path=input_file_path, file_format="xsf")
    structure.to(output_file_path=output_file_path, output_file_format="pwmat")


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
    opt2()