#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> PDOS & fatband structure "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat计算投影态密度、不同原子对态密度的贡献以及投影能带结构(算部分原子的态密度和投影能带）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/projected_DOS_and_band_structure.pdf
'''
    )

if __name__ == "__main__":
    opt3()