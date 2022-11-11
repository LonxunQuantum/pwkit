#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Boltzman-NAMD "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat模拟Boltzman NAMD（非绝热分子动力学）。NAMD模拟是一种广泛用于研究涉及激发态的载流子动力学过程的方法，如电荷弛豫、复合和输运。在这个Boltzman NAMD中，我们通过修改传统的密度矩阵，开发了一种新的NAMD模拟方法，它可以结合详细的平衡和退相干。（Boltzman NAMD可以考虑退相干效应和细致平衡，PWmat自带的job=NAMD没有考虑退相干和细致平衡）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/boltzman-NAMD.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt2()