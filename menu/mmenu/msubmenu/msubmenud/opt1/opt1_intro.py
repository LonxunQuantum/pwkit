#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> EMC "))
    print(
'''1.模块简介
----------
  该模块是PWmat和EMC（Effective mass calculator）之间的接口。EMC使用有限差分法（而不是带拟合法）计算带极值处的有效质量。该程序有两个版本：用FORTRAN和Python编写(算有效质量）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/EMC_guide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()