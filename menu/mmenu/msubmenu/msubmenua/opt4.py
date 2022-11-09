#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> ionic dieclectric contribution "))
    print(
'''1.模块简介
----------
  ionic dieclectric contribution
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_ionic_diel.pdf
'''
    )

if __name__ == "__main__":
    opt4()