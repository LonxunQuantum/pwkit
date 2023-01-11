import os


"""
def opta():
    '''
    Description
    -----------
        1. upf2upfSO.x 主要用于将 pwscf 的含有 spin-orbital 的赝势转换为 PWmat 专有
            数据格式的赝势。。
        2. upf2upfSO.x，之后就会得到相应的 SO 赝势
    '''
    current_path = os.getcwd()
    vwr_files_all_lst = []  # 所有的vwr的文件
    vwr_files_success_lst = []  # 成功转换的文件(.vwr -> .vwr.UPF)
    
    ### 1. 对现在文件路径下所有的 vwr 文件逐个进行转换
    for file_name in os.listdir(current_path):
        file_path = os.path.join(current_path, file_name)
        if os.path.isfile(file_path) and (file_name.split('.')[-1] == "vwr"):
            atom = file_name.split('.')[0]
            vwr_files_all_lst.append("{0}.vwr".format(atom))
        
            # Note: shell 程序出错，不会导致Python程序终结            
            os.system("echo {0}.vwr | vwr2upf.x".format(atom))
    
    ### 2. 检查是否生成了对应的 atom.vwr.UPF 文件
    for tmp_vwr_file in vwr_files_all_lst:
        file_path = os.path.join(current_path, file_name, ".UPF")
        if os.path.isfile(file_path):
            vwr_files_success_lst.append(tmp_vwr_file)
    
    ### 3. 输出 summary
    print_sum(vwr_files_all_lst=vwr_files_all_lst,
            vwr_files_success_lst=vwr_files_success_lst)


def print_sum(vwr_files_all_lst:list,
              vwr_files_success_lst:list):
    '''
    Description
    -----------
        1. 输出 summary
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 当前文件下所有的 vwr 文件:")
    for idx, file_name in enumerate(vwr_files_all_lst):
        print("\t\t{0:>2}. {1:<12}".format(idx, file_name))
    
    print("\t* 成功转换为 UPF 格式的文件为:")
    for idx, file_name in enumerate(vwr_files_success_lst):
        print("\t\t{0:>2}. {1:<12}".format(idx, file_name))
    
    print("*{0:-^68}*".format("---------"))



if __name__ == "__main__":
    opta()
"""