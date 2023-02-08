import os
import shutil


def opt4():
    '''
    Description
    -----------
        1. MOVEMENT格式 -> xsf格式
    
    Variables
    ---------
        1. input_file_path
        2. output_file_path
    '''
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    
    # 若不存在 MOVEMENT 文件，则需要手动指明 MOVEMENT 格式文件的文件名
    input_file_name = "MOVEMENT"
    input_file_path = os.path.join(current_path, input_file_name)
    while ( not os.path.exists(os.path.join(current_path, input_file_name)) ):
        os.system('''        echo -e "\n\033[31m - 未搜索到名为 {0} 的结构文件，需要手动指定MOVEMENT格式的文件名...\033[0m\n"'''.format(input_file_name))
        input_file_name = input(" MOVEMENT格式的文件名\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
    
    # e.g. output_file_name = "MOVEMENT.xsf"
    output_file_name = "MOVEMENT.xsf"
    output_file_path = os.path.join(current_path, output_file_name)
        

    ### Step 2. 文件格式转换
    os.system('echo "\033[36m - Tips: MOVEMENT文件格式转换需要稍等片刻...\033[0m"')
    os.system("$PWKIT_ROOT/menu/scripts/convert_from_config.x < {0} > /dev/null".format(input_file_name))


    ### Step 3. 输出程序运行的信息
    print_sum(input_file_name, output_file_name)
    os.remove("MOVEMENT.xyz")
    

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
    opt4()