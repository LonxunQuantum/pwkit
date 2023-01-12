import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^60}".format(" 数据可视化 "))
    print(
''' 1) plot_band_structure.x            2) plot_DOS.py
 3) absorption_spec_K2step.x         4) plot_wg.x
 5) plot_DOS_interp.x                6) plot_ABSORB_interp.x
 7) plot_TDDFT.x                     8) plot_fatband_structure.x
 9) plot_electrical_conductivity.x   a) plot_TDDFT_allk.x
 b) plot_TDDFT_rho.x'''
    )
    
    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    
if __name__ == "__main__":
    mmenu_cn()