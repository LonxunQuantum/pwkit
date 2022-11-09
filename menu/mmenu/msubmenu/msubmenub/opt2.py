#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Defect Nonradiative Decay "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何计算缺陷之间的非辐射衰减率。它提供了一种使用密度泛函理论计算对应于所有声子模式的电声耦合系数的方法(缺陷非辐射衰减）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/defect_nonradiative.pdf
'''
    )

if __name__ == "__main__":
    opt2()