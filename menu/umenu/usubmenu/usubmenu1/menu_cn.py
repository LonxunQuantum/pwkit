import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^60}".format(" 格式转换 "))
    print(
'''
 1) convert_rho.x            2) poscar2config.x
 3) cell2config.x            4) xsf2config.x
 5) pwscf2config.x           6) convert_from_config.x
 7) config2poscar.x          8) atominfo.x               
 9) convert_realwg.x         a) convert_wg2rho           
 b) convert_rho_multiply'''
    )
    
    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    mmenu_cn()