#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Boltzwann "))
    print(
'''1.模块简介
----------
  该模块是PWmat和Boltzwann之间的界面，可用于计算传输特性，包括电导率和导热率、塞贝克系数等。需要注意的是，BolztWann代码与Wannier90代码紧密集成。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Boltzwann.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt3()