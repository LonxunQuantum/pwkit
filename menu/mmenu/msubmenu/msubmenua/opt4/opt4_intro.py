#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> ionic dieclectric contribution "))
    print(
'''1.模块简介
----------
  计算介电常数离子部分的贡献，可以加上高频介电常数后得到低频介电常数。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_ionic_diel.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )


if __name__ == "__main__":
    opt4()