import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^48}".format("  其他格式 -> PWMat格式  "))
    print(
''' 1) POSCAR文件 -> PWMat文件     2) CELL文件 -> PWMat文件
 3) XSF文件 -> PWMat文件        4) pwscf文件  -> PWMat文件
 5) 
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