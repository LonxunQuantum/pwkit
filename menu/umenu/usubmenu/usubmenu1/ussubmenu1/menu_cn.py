import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^50}".format("  其他格式 -> PWMat格式  "))
    print(
''' 1) POSCAR文件 (POSCAR)     -> atom.config
 2) xsf文件    (atom.xsf)   -> atom.config
 3) atat文件   (rndstr.in)  -> atom.config     
 4) cif文件    (atom.cif)   -> atom.config     
 5) pwscf文件  (atom.pwscf) -> atom.config     
 6) cell文件   (atom.cell)  -> atom.config
 7) pdb文件    (atom.pdb)   -> atom.config     
 8) inp文件    (atom.inp)   -> atom.config
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