#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Virtual Crystal Approximation (VCA) Calculations "))
    print(
'''1.模块简介
----------
  该模块用于研究无序合金和具有近似无序处理的固溶体的电子能带结构。与超胞近似相比，该模块提供了一种更简单且计算成本更低的方法。通过使用这种虚晶近似（VCA）方法，可以很容易地计算无序合金和固溶体的晶格常数和电子结构。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_VCA.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )


if __name__ == "__main__":
    opt3()