#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Heisenberg exchange interaction constant "))
    print(
'''1.模块简介
----------
  该模块用于使用线性响应理论计算周期系统中两个特定位点之间海森堡模型中的交换相互作用常数。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Heisenberg_exchange_20220215.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt2()