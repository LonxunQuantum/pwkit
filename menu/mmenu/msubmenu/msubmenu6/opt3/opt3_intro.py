#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> PWphono3py "))
    print(
'''1.模块简介
----------
  该模块是PWmat和phonon3py之间的接口。Phonon3py可用于计算声子-声子相互作用和相关性质，包括晶格热导率、声子寿命/线宽和自能的虚部等。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/userguide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()