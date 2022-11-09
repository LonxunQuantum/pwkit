#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt6():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> pwmat_transport "))
    print(
'''1.模块简介
----------
  该模块用于使用PWmat和PWmat_transport程序计算弹性量子输运，该程序基于独特的量子散射计算方法。与标度为O（N3）的NEGF（非平衡格林函数）方法不同，这种散射状态方法直接计算给定能量下的散射状态。该方法与系统尺寸成线性比例，因此适用于大型系统仿真。它可以用于大型设备仿真，以取代TCAD等连续中介方法。该方法已用于研究量子隧穿晶体管，并已用于计算具有数千个铜原子的互连纳米结(使用散射态方法计算量子输运）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/pwmat_transport_doc.pdf
'''
    )

if __name__ == "__main__":
    opt6()