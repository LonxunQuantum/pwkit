#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^50}".format(" 格式转换 "))
    print(
''' 1) convert_rho.x            2) vwr2upf.x
 3) uspp2upf.x               4) poscar2config.x
 5) cell2config.x            6) xsf2config.x
 7) pwscf2config.x           8) convert_from_config.x
 9) config2poscar.x          a) upf2upfSO.x
 b) atominfo.x               c) convert_realwg.x
 d) convert_wg2rho           e) convert_rho_multiply'''
    )
    
    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    
if __name__ == "__main__":
    mmenu_cn()