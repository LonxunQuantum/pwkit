#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Electrical conductivity "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat根据Kubo Greenwood（KG）公式计算金属系统的电导率(使用Kubo-Greenwood方法计算金属体系的电导率，不适用半导体）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/plot_electrical_conductivity.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()