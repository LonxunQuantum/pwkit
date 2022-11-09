#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> PLUMED "))
    print(
'''1.模块简介
----------
  PLUMED是一个功能强大的软件，包括：增强的采样算法；自由能法；用于分析分子动力学（MD）模拟产生的大量数据的工具(使用元动力学计算表面自由能）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Plumed_intro.pdf
'''
    )

if __name__ == "__main__":
    opt1()