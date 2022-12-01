import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Water splitting "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用PWmat计算析氧反应（OER，水分解）、氧还原反应（ORR，燃料电池）、析氢反应（HER，水分解）。它包括如何计算中间态的吉布斯自由能和不同催化作用的火山曲线(几种常见的催化计算，OER/HER/ORR等）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/OER.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()