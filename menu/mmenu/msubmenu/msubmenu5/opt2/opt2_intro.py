import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> BANDUP "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用Bandup展开基于平面波的计算的能带。BandUP是一个代码，可以把超胞计算的波函数投影到原胞的相关k点上(可以算能带反折叠）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_bandup.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()