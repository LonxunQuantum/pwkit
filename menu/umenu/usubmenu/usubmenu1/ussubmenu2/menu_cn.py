import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^50}".format("  PWMat格式 -> 其他格式  "))
    print(
''' 1) atom.config -> POSCAR文件 (POSCAR)    
 2) atom.config -> xsf文件    (atom.xsf)
 3) atom.config -> atat文件   (rndstr.in)
 4) atom.config -> cif文件    (atom.cif)
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