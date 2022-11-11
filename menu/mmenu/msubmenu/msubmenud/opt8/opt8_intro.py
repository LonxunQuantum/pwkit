#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt8():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> NONEQUILIBRIUM_SCF "))
    print(
'''1.模块简介
----------
  在etot.input的job=SCF计算中，有泊松解的周期边界条件。但是在一个器件中，可以有不同的电极，它们有不同的电压，因此我们可能希望有固定边界值的泊松解(非平衡边界条件SCF计算）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/NONEQUILIBRIUM_SCF.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )  
  

if __name__ == "__main__":
    opt8()