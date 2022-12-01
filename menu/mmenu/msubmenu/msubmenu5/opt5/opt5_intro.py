import click


@click.command()
def opt5():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> U value calculation in LDA+U "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat获得LDA+U中的U值。（利用线性响应方法估算U值，相比传统取大量U值凑实验数据的方法更加地科学）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_U_value_calculation_20221024.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt5()