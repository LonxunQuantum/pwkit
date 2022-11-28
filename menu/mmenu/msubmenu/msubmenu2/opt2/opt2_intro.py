#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> disorder "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用disorder软件生成PWmat的不可约化位点占据构型。disorder是一个开源软件，设计用于生成不可约位点占据构型（即对称不等价无序晶体结构），可用于无序掺杂，包括取代掺杂和空位掺杂。disorder软件可以对输入晶胞进行任意扩包操作。最重要的是，实现了不可约构型数量与运行时间成线性比例，代码运行效率极高。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/disorder_manual.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )


if __name__ == "__main__":
    opt2()