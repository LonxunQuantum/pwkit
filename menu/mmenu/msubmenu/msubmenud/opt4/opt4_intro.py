import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> BoltzTraP "))
    print(
'''1.模块简介
----------
  该模块是PWmat和BoltzTrap之间的接口，可用于计算半经典输运系数。使用BoltzTrap，可以计算半导体热电材料的塞贝克系数、电导率弛豫时间比、电子热导率、电子热容和霍尔系数等。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_bolztrap_pwmat.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt4()