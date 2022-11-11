#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Charge trapping calculation "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用DFT+Marcus理论计算电荷俘获，包括两个状态之间的耦合常数、重组能量和电荷俘获率的计算。当与电荷修补方法相结合时，这种方法可以用于研究具有数万个原子的大系统。电荷转移是一个重要的过程，描述了一个电子从一个局域态跃迁到另一个局域态，这可能发生在局域态（例如，点缺陷）或扩展态到局域态之间。这是一个声子辅助过程，可以用朗道-齐纳跃迁来描述，也可以用马库斯理论或多声子过程来计算。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/ChargeTrapping-Module-4-29.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()