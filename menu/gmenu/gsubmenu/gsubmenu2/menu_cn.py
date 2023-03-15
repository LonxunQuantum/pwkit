import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^60}".format(" 结构转换 "))
    print(
''' 1) 其他格式 -> PWMat格式        2) PWMat格式 -> 其他格式
 3) 查看结构信息                 4) 按照原子序数整理atom.config
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