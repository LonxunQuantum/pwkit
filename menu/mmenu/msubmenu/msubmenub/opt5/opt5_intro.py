#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt5():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> anharmonic multi-phonon nonradiative transition "))
    print(
'''1.模块简介
----------
  半导体深中心的非辐射载流子捕获对于基础物理和器件工程都非常重要。该模块与模块13类似，我们提供了一种新的算法来搜索经典跃迁势垒，其中通过考虑缺陷不同电荷状态下的局部声子模式变化来校正非谐效应(非谐多声子非辐射跃迁）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/anharmonic%20multi-phonon%20nonradiative%20transition.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt5()