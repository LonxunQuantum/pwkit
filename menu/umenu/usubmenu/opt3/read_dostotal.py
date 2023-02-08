import os
import linecache
import copy
import pandas as pd 



def check_requisites():
    '''
    Description
    -----------
        1. 检查时候有 `plot_DOS.py` 所需的文件
                1) DOS.totalspin (这个文件未将费米能级归零)
                2) OUT.FERMI
    
    Return
    ------
        1. [mark_dos_totalspin, mark_out_fermi]: list
            1) mark_dos_totalspin: bool
                DOS.totalspin 是否存在
            2) mark_out_fermi: bool
                OUT.FERMI 是否存在
    '''
    current_path = os.getcwd()
    
    mark_dos_totalspin = os.path.exists(
                            os.path.join(current_path, "DOS.totalspin")
                        )
    mark_out_fermi = os.path.exists(
                            os.path.join(current_path, "OUT.FERMI")
                        )
    
    if mark_dos_totalspin and mark_out_fermi:
        # case 1. DOS.totalspin 和 OUT.FERMI 均存在
        pass
    else:
        if not mark_dos_totalspin:
            # case 2. DOS.totalspin 不存在
            os.system('echo "\033[31m - Error: DOS.totalspin 不存在\033[0m"')
    
    return [mark_dos_totalspin, mark_out_fermi]



def get_efermi(out_fermi_path:str):
    '''
    Description
    -----------
        1. 从 OUT.FERMI 中读取费米能级 (单位: eV)
    '''
    #  Fermi Energy =   -1.23104432294756       eV
    first_row = linecache.getline(out_fermi_path, 1)
    first_row_lst = first_row.split()
    efermi_ev = float( first_row_lst[-2] )
    return efermi_ev


def get_dos_df(dos_totalspin_path:str):
    '''
    Description
    -----------
        1. 从 DOS.totalspin 中读取数据，初始化一个 pd.Dataframe对象
    '''
    ### Step 1. 删除 DOS.totalspin 行首的 "#"
    with open(dos_totalspin_path, "r") as f:
        all_rows = f.readlines()
        # first_row: "#  Energy  Total  Mo-s  Mo-p  Mo-s  Mo-d  S-s  S-p"
        first_row = all_rows[0]
        first_row_lst = first_row.split()
        try:
            first_row_lst.remove("#")    # 删除行首的"#"
        except:
            pass
        new_first_row = "\t   ".join(first_row_lst)
        new_first_row += "\n"   # 'Energy\tTotal\tMo-s\tMo-p\tMo-s\tMo-d\tS-s\tS-p\n'
        all_rows.pop(0) # 删除原来的行首
        all_rows.insert(0, new_first_row)   # 添加新的行首
    
    ### Step 2. 写入新的 DOS.totalspin 到新文件 `DOS.totalspin_`
    current_path = os.path.dirname(dos_totalspin_path)
    new_dos_totalspin_path = os.path.join(current_path, "DOS.totalspin.bak")
    with open(new_dos_totalspin_path, "w") as f:    # mode="w" 重写模式
        f.writelines(all_rows)        
    
    ### Step 3. 读取 DOS.totalspin 的数据，获取 pd.DataFrame 对象
    df_dos = pd.read_csv(new_dos_totalspin_path, sep='\s+')
    
    ### Step 4. 删除中间文件(temp file) -- DOS.totalspin.bak
    os.remove(new_dos_totalspin_path)
    
    return df_dos
    
    

def get_dfs_dos():
    '''
    Description
    -----------
        1. 读取 DOS.totalspin 和 OUT.FERMI，生成以下对象，用于绘制 dos
    
    Return
    -------
        Case 1. [df_dos, df_dos_sub_efermi]: list of pd.DataFrame
                1. df_dos: pd.DataFrame
                    - 未减去费米能级
                2. df_dos_sub_efermi: pd.DataFrame
                    - 减去费米能级
                    
        Case 2. [df_dos]: pd.DataFrame
                    - 未减去费米能级
        
    
    Requisites
    ---------
        1. DOS 文件： DOS.totalspin
        2. 费米能级文件：OUT.FERMI
        
        
    Steps
    -----
        1. 检查是否存在 DOS.totalspin
        2. 如果存在 OUT.FERMI，则到费米能级
        3. 读取 DOS.totalspin 的信息，生成 pd.DataFrame 对象
    '''
    current_path = os.getcwd()
    ### Step 1. 检查 requisite files，如果不满足条件，自动退出程序
    #       mark_dos_totalspin: DOS.totalspin 是否存在
    #       mark_out_fermi: OUT.FERMI 是否存在
    mark_dos_totalspin, mark_out_fermi = check_requisites()
    if not mark_dos_totalspin:
        raise SystemExit
        
    ### Step 2. 得到费米能级（如果 OUT.FERMI 存在的话）
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    if mark_out_fermi:
        # 如果 OUT.FERMI 存在``
        efermi = get_efermi(out_fermi_path=out_fermi_path)

    ### Step 3. 读取 DOS.totalspin 文件，生成 pd.DataFrame 对象
    dos_totalspin_path = os.path.join(current_path, "DOS.totalspin")
    df_dos = get_dos_df(dos_totalspin_path=dos_totalspin_path)
    
    ### Step 4. 读取 DOS.totalspin 文件，减去费米能级后，生成 pd.DataFrame 对象
    df_dos_sub_efermi = copy.deepcopy(df_dos)
    if mark_out_fermi:
        # 如果 OUT.FERMI 存在
        df_dos_sub_efermi.loc[:, "Energy"] = \
                        df_dos_sub_efermi.loc[:, "Energy"] - efermi
    
    if mark_out_fermi:
        return [df_dos, df_dos_sub_efermi]
    else:
        return [df_dos]


if __name__ == "__main__":
    df_dos, df_dos_ = get_dfs_dos()
    print(df_dos)
    print(df_dos_)