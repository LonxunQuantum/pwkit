#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Charge Patching Method introduction (CPM) "))
    print(
'''1.模块简介
----------
  本模块用于介绍什么是CPM，以及哪些CPM可以用于他们的研究。CPM是计算大型纳米系统的一种通用方法，它从小型系统计算中生成大型系统的电荷密度（即DFT哈密顿量）。它还包括一套计算大系统哈密顿量电子结构的方法。简而言之，如果你正在计算具有数千个或数万个原子的纳米结构，特别是它们的电子和光学性质，甚至动力学行为，那么CPM将是有用的。（CPM方法的功能介绍）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/CPM_introduction.pdf
'''
    )

if __name__ == "__main__":
    opt2()