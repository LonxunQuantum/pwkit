#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> PyPWmat "))
    print(
'''1.模块简介
----------
  该模块是PWmat和Phonopy之间的接口。Phonopy是一个用于谐波和准谐波声子计算的开源软件包。它可以用于计算声子带结构、声子DOS和部分DOS、声子热性质等。最重要的是，该模块可以计算缺陷系统的声子和子系统的声子模(算声子谱，缺陷声子谱，部分原子声子谱）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/PyPWmat_guide_20220316.pdf
'''
    )

if __name__ == "__main__":
    opt1()