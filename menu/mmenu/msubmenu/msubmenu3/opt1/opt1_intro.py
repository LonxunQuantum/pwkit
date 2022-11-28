#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> RINGS "))
    print(
'''1.模块简介
----------
  该模块是PWmat和RINGS（Rigorous Investigation of Networks Generated using Simulations）之间的接口。RINGS是在Fortran90/MPI中开发的科学代码，用于分析分子动力学模拟的结果。使用R.I.N.G.S.代码可以计算：半径分布函数；模拟中子和X射线结构因子；均方位移；键角和二面角分布；粘结性能；结构环境分布；空隙分布；非常详细的环统计分析；使用OpenDX进行三维可视化的各种输入文件。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/RINGS.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()