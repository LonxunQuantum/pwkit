#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^80}".format(" Module --> Genetic algorithm to search global minimum structure "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用遗传算法搜索生成被吸收分子/簇的新结构，同时保持底物的结构
不变（尽管它在松弛过程中会移动）。例如，它可以用于搜索：吸附在Cu（111）表面的CO周
围的水分子；具有给定原子数的金属簇；两种材料界面区的原子结构；平坦金属表面上的水分
子；球形金属纳米团簇上的水分子...（用基因遗传算法搜索表面结构，例如用于表面催化）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/GA%20Algorithm.pdf
'''
    )

if __name__ == "__main__":
    opt3()