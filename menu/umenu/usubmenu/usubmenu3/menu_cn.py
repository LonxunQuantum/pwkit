#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^60}".format(" 数据后处理 "))
    print(
''' 1) add_field.x             2) split_kp.x
 3) NAMD_psi.x              4) NAMD_Boltzman.x
 5) ug_moment.x             6) vacuum.x
 7) bandgap                 8) nonradiative.x   
 9) plot_tddft_absorp.x     a) TDM.x
'''
    )
    
    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    
if __name__ == "__main__":
    mmenu_cn()