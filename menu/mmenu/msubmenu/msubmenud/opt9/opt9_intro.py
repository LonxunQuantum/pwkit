#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt9():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Spin Hall Effect (SHC) "))
    print(
'''1.模块简介
----------
  自旋霍尔效应主要是由SOC引起的，自旋向上的电子和自旋向下的电子会朝相反的方向移动，因此在垂直于外部电场的方向上没有电流流动(算自旋霍尔电导）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_SHC.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt9()