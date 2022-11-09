#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Auger Decay Rate calculation "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat计算孤立系统（分子或量子点）中的俄歇衰变率（俄歇效应的可能性）。俄歇过程是一个通过库仑相互作用的过程，当一个电子从较高能级下降到较低能级时，能量转移到另一个电子，该电子从一个较低能级激发到较高能级。这个模块专注于电离，这意味着最终状态是真空状态。（计算俄歇复合）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Auger_Deca_%20Rate.pdf
'''
    )

if __name__ == "__main__":
    opt2()