#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> electron-phonon coupling (EPC) "))
    print(
'''1.模块简介
----------
  使用瓦尼尔函数（wannier functions, WFs）计算电声耦合矩阵。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_EPC.pdf
'''
    )

if __name__ == "__main__":
    opt1()