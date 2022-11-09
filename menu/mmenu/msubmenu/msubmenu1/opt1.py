#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click
import sys


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> CALYPSO "))
    print(
'''1.模块简介
----------
  该模块是PWmat和CALYPSO之间的接口，CALYPSO是一种有效的结构预测方法及其同名计算软件。该方法只需要给定化合物的化学成分，便可以预测给定外部条件下的稳定或亚稳结构，因此CALYPSO软件包可用于预测/确定晶体结构和设计多功能材料（结构搜索）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/calypso.pdf
'''
    )

if __name__ == "__main__":
    opt1()