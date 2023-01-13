import os
import shutil


def opt1():
    '''
    Description
    -----------
        1. convert_rho.x 主要是把 PWmat 输出的二进制文件 OUT.RHO、OUT.VR 转换为 VESTA、
        XcrySDen 可读的格式。
        2. `convert_rho.x OUT.RHO`   
            - 之后就会得到 RHO.xsf
        
    Variables
    ---------
        1. input_file_path
        2. output_file_path
    '''    
    mark_rho_exits = False
    
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    try: # 删除原本存在的 RHO.xsf
        shutil.rmtree(os.path.join(current_path, "RHO.xsf"))
    except:
        pass
    
    for file_name in os.listdir(current_path):
        file_path = os.path.join(current_path, file_name)
        # 默认输入 OUT.RHO 文件，进行格式转换        
        if os.path.isfile(file_path) and (file_name=="OUT.RHO"):
            input_file_name = "OUT.RHO"
            input_file_path = file_path
            mark_rho_exits = True
            break
    
    # 若不存在 OUT.RHO 文件，则需要手动指明 OUT.RHO 格式文件的文件名
    if mark_rho_exits == False:
        os.system('''        echo -e "\n\033[31m - 未搜索到名为OUT.RHO的文件，需要手动指定OUT.RHO格式的文件名...\033[0m\n"''')
        input_file_name = input(" OUT.RHO格式的文件名\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
    
    # e.g. output_file_name = "atom.config"
    output_file_name = "RHO.xsf"
    output_file_path = os.path.join(current_path, output_file_name)
        
    
    ### Step 2. 文件格式转换
    os.system("convert_rho.x {0}".format(input_file_name))


    ### Step 3. 输出程序运行的信息
    rho_xsf_file_path = os.path.join(current_path, "RHO.xsf")
    if os.path.exists(rho_xsf_file_path): # os.system() 中的cmd执行成功
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
    opt1()