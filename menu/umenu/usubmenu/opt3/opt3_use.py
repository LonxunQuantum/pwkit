import os 
import matplotlib.pyplot as plt

from read_dostotal import (
                    check_requisites, 
                    get_efermi,
                    get_dos_df, 
                    get_dfs_dos,
                    )


def opt3():
    '''
    Description
    -----------
        1. 生成文件:
            - DOS.totalspin.csv : 未减去费米能级
            - DOS.totalspin_ShiftFermi.csv : 减去费米能级
            - DOS.jpg: Total Dos 图像 (未减去费米能级的)
            - DOS_ShiftFermi.jpg: Total Dos 图像 (减去费米能级的)
    '''
    E_min = -5
    E_max = 5
    ### Note
    ### ----
    ###     1. 如果当前文件夹下没有 OUT.FERMI，则输出的 DOS 无法减去费米能级
    current_path = os.getcwd()
    
    df_dos, df_dos_minus_efermi  = get_dfs_dos()
    try:
        assert (df_dos_minus_efermi == False)
        marks_lst = [True, False]
    except ValueError:
        marks_lst = [True, True]

    ### Step 1. Plot TDOS
    ### Step 1.1. 全局设置
    #plt.rcParams["font.family"] = "Times New Roman"
    #plt.rcParams['mathtext.fontset'] = 'custom'
    #plt.rcParams['mathtext.rm'] = 'Times New Roman'
    #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
    #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
    ### Step 1.2. 刻度线朝内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    
    ### Step 1.3. Plot TDOS （未减去费米能级的 TDOS)
    plt.figure(figsize=(10, 8))
    mask = (df_dos.loc[:, "Energy"] >= E_min) & (df_dos.loc[:, "Energy"] <= E_max)
    df_dos = df_dos.loc[mask, :]
    plt.plot(
            df_dos.loc[:, "Energy"],
            df_dos.loc[:, "Total"],                
            c="indigo",
            lw="2",
            )
    # 1. xlabel / ylabel
    plt.xlabel("Energy (eV)", 
               fontsize=28,
               fontweight="bold")
    plt.ylabel("DOS",
               fontsize=28,
               fontweight="bold")
    # 2. xticks / yticks
    plt.xticks(fontsize=20, 
        fontweight="bold"
        )
    plt.yticks(fontsize=20, 
        fontweight="bold"
        )
    # 3. 刻度线的粗细
    plt.tick_params(
        width=2,        # 刻度线的粗细
        length=5,       # 刻度线的长短
        #labelsize=28   # 刻度线的字体大小
        )
    # 4. 设置坐标轴的粗细
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(1.5);###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(1.5);####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(1.5);###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(1.5);###设置右边坐标轴的粗细
    # 5. xrange
    #delta = float(0.05 * (max-min))
    #min = min - delta
    #max = max + delta/dos
    plt.xlim(E_min, E_max)
    
    # 6. 保存图片
    plt.savefig(
                os.path.join(current_path, "dos.jpg"),
                dpi=300,
                bbox_inches="tight",
                )
    
    
    ### Step 2. Plot TDOS (绘制减去费米能级的TDOS)
    if marks_lst[1]:
        ### Step 2.1. 全局设置
        #plt.rcParams["font.family"] = "Times New Roman"
        #plt.rcParams['mathtext.fontset'] = 'custom'
        #plt.rcParams['mathtext.rm'] = 'Times New Roman'
        #plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
        #plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
        ### Step 2.2. 刻度线朝内
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        
        ### Step 2.3. Plot TDOS （未减去费米能级的 TDOS)
        plt.figure(figsize=(10, 8))
        mask = (df_dos_minus_efermi.loc[:, "Energy"] >= E_min) & (df_dos_minus_efermi.loc[:, "Energy"] <= E_max)
        df_dos_minus_efermi = df_dos_minus_efermi.loc[mask, :]
        plt.plot(
                df_dos_minus_efermi.loc[:, "Energy"],
                df_dos_minus_efermi.loc[:, "Total"],
                c="indigo",
                lw="2",
                )
        # 1. xlabel / ylabel
        plt.xlabel("Energy (eV)", 
                fontsize=28,
                fontweight="bold")
        plt.ylabel("DOS",
                fontsize=28,
                fontweight="bold")
        # 2. xticks / yticks
        plt.xticks(fontsize=20, 
            fontweight="bold"
            )
        plt.yticks(fontsize=20, 
            fontweight="bold"
            )
        # 3. 刻度线的粗细
        plt.tick_params(
            width=2,        # 刻度线的粗细
            length=5,       # 刻度线的长短
            #labelsize=28   # 刻度线的字体大小
            )
        # 4. 设置坐标轴的粗细
        ax = plt.gca()
        ax.spines['bottom'].set_linewidth(1.5); ###设置底部坐标轴的粗细
        ax.spines['left'].set_linewidth(1.5);   ####设置左边坐标轴的粗细
        ax.spines['right'].set_linewidth(1.5);  ###设置右边坐标轴的粗细
        ax.spines['top'].set_linewidth(1.5);    ###设置右边坐标轴的粗细
        # 5. xrange / yrange
        #delta = float(0.05 * (max-min))
        #min = min - delta
        #max = max + delta/dos
        plt.xlim(E_min, E_max)
        #plt.ylim(-5, 5)
        if marks_lst[1]:
            plt.savefig(
                        os.path.join(current_path, "dos_ShiftFermi.jpg"),
                        dpi=300,
                        bbox_inches="tight",
                        )
    
    
    ### Step 3. 保存 csv 文件
    current_path = os.getcwd()
    ### Step 3.1. 保存 csv 文件
    df_dos.to_csv(
            os.path.join(current_path, "DOS.totalspin.csv"),
            sep=',',
            index=False,
            )
    if marks_lst[1]:
        df_dos_minus_efermi.to_csv(
                os.path.join(current_path, "DOS.totalspin_ShiftFermi.csv"),
                sep=',',
                index=False,
                )
    
    ### Step 3.2. 保存图片`` (绘制完成后就保存完毕)
    ### ...
    
    ### Step 4. Summary
    print_sum(marks_lst)


def print_sum(marks_lst):
    '''
    Description
    -----------
        1. 在 terminal 中输出:
            - 输入文件
            - 输出文件
    
    Parameters
    ----------
        1. marks_lst:
            - [True, True]
            - [True, False]
    '''
    print("*{0:-^68}*".format( " Summary "))
    
    print("\t* 输入文件:", end='\t')
    print(" - {0}".format("DOS.totalspin"))
    if marks_lst[1]:
        print(" \t\t\t - {0}".format("OUT.FERMI"))

    # p1
    print("\t* 输出文件:", end='\t')
    # p2
    print(" - {0}".format("DOS.totalspin.csv"))
    # p3
    if marks_lst[1]:
        print(" \t\t\t - {0}".format("DOS.totalspin_ShiftFermi.csv"))
    print(" \t\t\t - {0}".format("dos.jpg"))
    # p4
    if marks_lst[1]:
        print(" \t\t\t - {0}".format("dos_ShiftFermi.jpg"))   
    
    print("*{0:-^68}*".format("---------"))
    

if __name__ == "__main__":
    opt3()