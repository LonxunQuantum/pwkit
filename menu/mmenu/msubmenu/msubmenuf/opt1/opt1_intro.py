#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> YAMBO "))
    print(
'''1.模块简介
----------
  该模块用于介绍如何运行YAMBO以基于PWmat DFT结果获得GW准粒子能量。YAMBO实施了多体微扰理论（MBPT）方法（如GW和BSE）和时间相关密度泛函理论（TDDFT），这允许精确预测半导体的带隙、带对准、缺陷准粒子能量、光学和材料的非平衡特性等基本特性(介绍如何使用pwmat+yambo进行GW计算）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/YAMBO_GW.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()