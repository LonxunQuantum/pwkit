import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> TDDFT Carrier Cooling "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用rt-TDFT模拟超快动力学，包括系统突然失去电子后的动力学（例如，由于飞秒激光束引起的电离）；或将一个电子从价带激发到一个导带态；一个非常快的离子碰撞（TDDFT算载流子冷却）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/TDDFT_Carrier_cooling.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()