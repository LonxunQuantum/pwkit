#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> pw_absorption "))
    print(
'''1.模块简介
----------
  用于计算dynamic charge（大部分情况下相当于born charge） 和声子吸收（忽略了屏蔽效应）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide.pdf
'''
    )

if __name__ == "__main__":
    opt4()