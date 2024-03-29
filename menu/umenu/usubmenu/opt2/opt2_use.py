import os
import shutil
import linecache


def opt1():
    '''
    Description
    -----------
        1. plot_wg2.x 主要用于将 OUT.WG 转换为可视化的文件 (partialcharge.xsf) 放在 VESTA 里面查看。
        2. `plot_wg2.x`
            - 之后就会得到 partialcharge.xsf
        
    Variables
    ---------
        1. input_file_path
        2. output_file_path
        
    Requisites
    ----------
        1. 结构文件：atom.config 格式文件
        2. 波函数文件：OUT.WG 格式文件
        
    Note
    ----
        1. `plot_wg.x`: 绘制单个kpoint、单个波函数的电荷 (rho)
        2. `plot_wg2.x`: 绘制单个kpoint、序号连续的多个波函数的电荷 (rho)
    '''        
    ### Step 1. 得到输入输出格式的文件
    current_path = os.getcwd()
    try: # 删除原本存在的 partialcharge.xsf
        shutil.rmtree(os.path.join(current_path, "partialcharge.xsf"))
    except:
        pass

    wg_file_name = input(" 请输入 OUT.WG 格式的文件名\n ------------>>\n")
    
    # e.g. output_file_name = "partialcharge.xsf"
    output_file_name = "partialcharge.xsf"
    
    
    ### Step 2. 用户手动输入 plot_wg2.x 的参数
    ##  Step 2.1. 从 REPORT 中查询 NUM_KPT 和 NUM_BAND
    report_file_path = os.path.join(current_path, "REPORT")
    aim_content_kpt = "NUM_KPT"
    idx_row_kpt = search_aim(file_path=report_file_path, aim_content=aim_content_kpt)[0]
    #print(idx_row_kpt)
    num_kpt = linecache.getline(report_file_path, idx_row_kpt).split()[-1]
            
    report_file_path = os.path.join(current_path, "REPORT")
    aim_content_wg = "NUM_BAND"
    idx_row_wg = search_aim(file_path=report_file_path, aim_content=aim_content_wg)[0]
    #print(idx_row_wg)
    num_band = linecache.getline(report_file_path, idx_row_wg).split()[-1]
    
    
    ##  Step 2.2. 得到 plot_wg2.x 的各种信息
    ##             1. kpoint 的 index 
    ##             2. OUT.WG 格式的文件名
    ##             3. atom.config 格式的文件名
    ##             4. 波函数的 range of index
    # 1. OUT.WG 格式的文件名： 在前面
    
    # 2. atom.config 格式的文件
    #atom_config_name = "atom.config"    # 默认结构文件名为 atom.config
    #while ( not os.path.exists( os.path.join(current_path, atom_config_name) ) ):
    #    os.system('echo -e "\n\033[31m - 未搜索到 {0} 文件，需要手动指定结构文件的文件名...\033[0m\n"'.format(atom_config_name))
    atom_config_name = input(" 请输入 atom.config 格式的文件名\n ------------>>\n")
    
    # 3. kpoint 的 index
    idx_kpoint = input(" 一共有{0}个K点，请输入要画的K点 (e.g. `3`)\n ------------>>\n".format(num_kpt))
    
        
    # 4. 波函数的index (e.g. `12,16`)
    idx_wg = input(" 一共有{0}个波函数，请输入要画的波函数 (e.g. `12,16 or 12`)\n ------------>>\n".format(num_band))
    
        
    ### Step 3. 文件格式转换 (plot_wg2.x)
    if (',' in idx_wg) or \
        (idx_wg.split() != 1) or \
        ('-' in idx_wg) or \
        ('~' in idx_wg):
        if (idx_wg.split() != 1):
            idx_wg = ','.join( [value.strip() for value in idx_wg.split()] )
        if ('-' in idx_wg):
            idx_wg = ','.join( [value.strip() for value in idx_wg.split('-')] )
        if ('~' in idx_wg):
            idx_wg = ','.join( [value.strip() for value in idx_wg.split('-')] )
        
        os.system('echo -e "{0}\n{1}\n{2}\n{3}\n" | $PWKIT_ROOT/menu/scripts/plot_wg2.x > /dev/null'.format(
                                            idx_kpoint,
                                            wg_file_name,
                                            atom_config_name,
                                            idx_wg,            
                                            )
                )
    else:
        os.system('echo -e "{0}\n{1}\n{2}\n{3}\n" | $PWKIT_ROOT/menu/scripts/plot_wg.x > /dev/null'.format(
                                            idx_kpoint,
                                            wg_file_name,
                                            atom_config_name,
                                            idx_wg,            
                                            )
                )


    ### Step 4. 输出程序运行的信息    
    if os.path.exists(os.path.join(current_path, "PSI.xsf")): # os.system() 中的cmd执行成功
        os.system("mv PSI.xsf partialcharge.xsf")
        print_sum(atom_config_name=atom_config_name,
                  wg_file_name=wg_file_name,
                  idx_kpoint=idx_kpoint,
                  idx_wg=idx_wg,
                  output_file_name=output_file_name,
                  )
    else:
        print("Error!")
    

def print_sum(
            atom_config_name:str,
            wg_file_name:str,
            idx_kpoint:str,
            idx_wg:str,
            output_file_name:str="partialcharge.xsf",
            ):
    '''
    Description
    -----------
        1. 输出 summary
    
    Parameters
    ----------
        1. atom_config_name: str
            - atom.config 格式的结构文件名
            
        2. wg_file_name: str
            - OUT.WG 格式的文件名
            
        3. idx_kpoint: str
            - K点的 index e.g. `3`
            
        4. id_wg: str
            - 波函数的范围， e.g. `12,16`
        
        5. output_file_name: str
            - `partialcharge.xsf`
    '''
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入的结构文件  :", end="")
    print("\t{0}".format(atom_config_name))
    print("\t* 输入的波函数文件:", end="")
    print("\t{0}".format(wg_file_name))
    print("\t* 要画的K点       :", end="")
    try:
        print( "\t{0} ~ {1}".format(idx_kpoint.split(',')[0].strip(), idx_kpoint.split(',')[1].strip()) )
    except IndexError:
        print( "\t{0}".format(idx_kpoint.strip()) )
    
    print("\t* 要画的波函数    :", end="")
    try:
        print("\t{0} ~ {1}".format(idx_wg.split(',')[0].strip(), idx_wg.split(',')[1].strip()))
    except:
        print( "\t{0}".format(idx_wg.strip()) )
    print("\t* 输出文件        :", end="")
    print("\t{0}".format(output_file_name))
        
    print("*{0:-^68}*".format("---------"))


def search_aim(file_path:str, aim_content:str):
    '''
    Description
    -----------
        1. 查询文件中是否存在特定内容，并确定所在的行数
    
    Parameters
    ----------
        1. file_path: str

        2. aim: str

    '''
    with open(file_path) as f:
        lines_lst = f.readlines()
    idxs_lst = []
    for idx, line in enumerate(lines_lst, 1):
        if aim_content in line:
            idxs_lst.append(idx)
    return idxs_lst



if __name__ == "__main__":
    opt1()