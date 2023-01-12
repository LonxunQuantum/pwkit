import os



def opt3():
    '''
    Description
    -----------
        1. 把 PEtot 需要的 uspp 赝势格式转换为 PWmat 需要的 UPF 格式
        2. uspp2upf.x atom.uspp，之后就会得到 atom.uspp.UPF
    '''
    current_path = os.getcwd()
    uspp_files_all_lst = []  # 所有的 uspp 的文件
    uspp_files_success_lst = []  # 成功转换的文件(.uspp -> .uspp.UPF)
    
    ### 1. 对现在文件路径下所有的 vwr 文件逐个进行转换
    for file_name in os.listdir(current_path):
        file_path = os.path.join(current_path, file_name)
        if os.path.isfile(file_path) and (file_name.split('.')[-1] == "uspp"):
            atom = file_name.split('.')[0]
            uspp_files_all_lst.append("{0}.uspp".format(atom))
        
            # Note: shell 程序出错，不会导致Python程序终结            
            os.system("echo {0}.uspp | uspp2upf.x".format(atom))
    
    ### 2. 检查是否生成了对应的 atom.uspp.UPF 文件
    for tmp_uspp_file in uspp_files_all_lst:
        file_path = os.path.join(current_path, file_name, ".UPF")
        if os.path.isfile(file_path):
            uspp_files_success_lst.append(tmp_uspp_file)
    
    ### 3. 输出 summary
    print_sum(uspp_files_all_lst=uspp_files_all_lst,
            uspp_files_success_lst=uspp_files_success_lst)


def print_sum(uspp_files_all_lst:list,
              uspp_files_success_lst:list):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 当前文件下所有的 uspp 文件:")
    for idx, file_name in enumerate(uspp_files_all_lst):
        print("\t\t{0:>2}. {1:<12}".format(idx, file_name))
    
    print("\t* 成功转换为 UPF 格式的文件为:")
    for idx, file_name in enumerate(uspp_files_success_lst):
        print("\t\t{0:>2}. {1:<12}".format(idx, file_name))
    
    print("*{0:-^68}*".format("---------"))
    

if __name__ == "__main__":
    opt3()