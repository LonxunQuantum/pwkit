import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^50}".format("  PWMat格式 -> 其他格式  "))
    print(
''' 1) PWMat文件 -> POSCAR文件     2) PWMat文件 -> xsf文件
 3) PWMat文件 -> atat文件       4) PWMat文件 -> cif文件
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