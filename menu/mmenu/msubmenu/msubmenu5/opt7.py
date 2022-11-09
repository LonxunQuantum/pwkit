#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt7():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Band structure calculation by WKM "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用Wannier-Koopmans Method（WKM）计算基于Koopman定理的电子结构。几种LDA计算测试已应用于常见的共价半导体、离子晶体和有机晶体。带隙结果与实验结果吻合较好。（使用WKM计算电子结构， 对普通共价半导体，离子晶体和有机晶体都有很好的效果，对含d电子的体系还需要优化）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Wannier_Koopmans_Method.pdf
'''
    )

if __name__ == "__main__":
    opt7()