#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Pourbaix diagram "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat计算pourbaix图。Pourbaix图是材料a在不同电极电位U和pH值下的水下相稳定性图。在不同的（U，pH）点，A的最稳定形式可能是A1、A2、(布拜图计算，可以研究化学腐蚀等问题）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Pourbaix_diagram.pdf
'''
    )

if __name__ == "__main__":
    opt1()