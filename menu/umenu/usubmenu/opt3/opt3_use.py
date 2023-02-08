import os


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
        return [mark_dos_totalspin, mark_out_fermi]
    else:
        if not mark_dos_totalspin:
            # case 2. DOS.totalspin 不存在
            os.system('echo "\033[31m - Error: DOS.totalspin 不存在\033[0m"')
        if not mark_out_fermi:
            # case 3. OUT.FERMI 不存在
            os.system('echo "\033[31m - Error: OUT.FERMI 不存在\033[0m"')
        return [mark_dos_totalspin, mark_out_fermi]


def opt3():
    '''
    Description
    -----------
        1. plot_DOS.py 主要用于输出 DOS 图。
        2. 如果计算目录中有 OUT.FERMI 文件，那么可以通过运行 plot_DOS.py 脚本得到
        费米能级归零的结果 DOS.totalspin_ShiftFermi。
        
    
    Requisites
    ---------
        1. DOS 文件： DOS.totalspin
        2. 费米能级文件：OUT.FERMI
    '''
    ### Step 1. 检查 requisite files
    mark_dos_totalspin, mark_out_fermi= check_requisites()
    if not (mark_dos_totalspin and mark_out_fermi):
        raise SystemExit
        
    ### Step 2. 绘制 DOS

    



if __name__ == "__main__":
    opt3()