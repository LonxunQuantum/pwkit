#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Defect Level "))
    print(
'''1.模块简介
----------
  该模块用于计算半导体中的缺陷能级。晶体半导体中的缺陷能级一般是相对于价带最大值（VBM）或体导带最小值位置（CBM）。缺陷能级的典型图表示形成能作为费米能的函数。对于不同电荷缺陷，两条不同电荷线的交叉点是过渡能级(计算半导体中的缺陷能级）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Defect_calculation.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()