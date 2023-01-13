import os
import shutil


def opt1():
    '''
    Description
    -----------
        1. plot_wg.x 主要用于将 OUT.WG 转换为可视化的文件放在 VESTA 里面查看
        2. `plot_wg.x`   
            - 输入: OUT.WG
            - 输出: PSI.xsf
        
    Variables
    ---------
        1. input_file_path
        2. output_file_path
    '''    
    mark_wg_exits = False
    
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    try: # 删除原本存在的 PSI.xsf
        shutil.rmtree(os.path.join(current_path, "PSI.xsf"))
    except:
        pass
    
    for file_name in os.listdir(current_path):
        file_path = os.path.join(current_path, file_name)
        # 默认输入 OUT.WG 文件，进行格式转换        
        if os.path.isfile(file_path) and (file_name=="OUT.WG"):
            input_file_name = "OUT.WG"
            input_file_path = file_path
            mark_wg_exits = True
            break
    
    # 若不存在 OUT.WG 文件，则需要手动指明 OUT.WG 格式文件的文件名
    if mark_wg_exits == False:
        os.system('''        echo -e "\n\033[31m - 未搜索到名为OUT.WG的文件，需要手动指定OUT.WG格式的文件名...\033[0m\n"''')
        input_file_name = input(" OUT.WG格式的文件名\n------------>>\n")
        input_file_path = os.path.join(current_path, input_file_name)
    
    # e.g. output_file_name = "atom.config"
    output_file_name = "PSI.xsf"
    output_file_path = os.path.join(current_path, output_file_name)
        
    
    ### Step 2. 文件格式转换
    os.system("plot_wg.x")


    ### Step 3. 输出程序运行的信息
    wg_xsf_file_path = os.path.join(current_path, "PSI.xsf")
    if os.path.exists(wg_xsf_file_path): # os.system() 中的cmd执行成功
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