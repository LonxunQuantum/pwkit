import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> BSE-YAMBO "))
    print(
'''1.模块简介
----------
  该模块用于使用YAMBO+PWmat计算BSE的光学波谱（使用PWmat+yambo计算BSE，也可以算gw+bse）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/BSE-YAMBO.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()