#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click
import sys


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> USPEX "))
    print(
'''1.模块简介
----------
  该模块是PWmat和USPEX之间的接口。USPEX是Oganov实验室自2004年以来开发的一种方法，只需要输入材料的化学成分，就可以预测任意P-T条件下的晶体结构。除了晶体结构预测，USPEX还可以预测纳米颗粒、聚合物、表面、界面和2D晶体的结构（结构搜索软件USPEX的接口）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/PWmatUSPEX.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()