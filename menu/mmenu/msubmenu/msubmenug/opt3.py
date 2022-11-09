#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Cross Section calculation "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat计算高能电子束的电离截面。横截面是指电子碰撞电离的概率。这个模型使用一个称为二元偶极子（BED）模型的通用模型来计算电子碰撞电离过程的横截面。该横截面描述了另一个电子从材料中被踢出进入真空的过程。（计算电离截面）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Cross_Section.pdf
'''
    )

if __name__ == "__main__":
    opt3()