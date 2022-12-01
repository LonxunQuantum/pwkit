import click


@click.command()
def opt5():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Anomalous Hall Conductivity（AHC）calculation "))
    print(
'''1.模块简介
----------
  该模块用于使用PWmat和wannier90计算反常霍尔电导。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/AHC.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt5()