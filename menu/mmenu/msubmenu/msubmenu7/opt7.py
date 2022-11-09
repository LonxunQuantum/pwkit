#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt7():
    ### Part I. 模块名
    print("{0:=^80}".format(" Module --> excitionic state "))
    print(
'''1.模块简介
----------
  该模块用于通过求解两粒子哈密顿量的secular equation来计算量子点中的激子态，还可
以获得吸收光谱和diplole matrix。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/exciton.pdf
'''
    )

if __name__ == "__main__":
    opt7()