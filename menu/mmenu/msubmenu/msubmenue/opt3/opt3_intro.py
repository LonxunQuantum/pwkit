import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Ion collision simulation by rt-TDDFT "))
    print(
'''1.模块简介
----------
  本模块介绍如何生成带电离子，适用tddft模拟离子辐照、碰撞、注入等。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/ion%20collision%20using%20TDDFT.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()