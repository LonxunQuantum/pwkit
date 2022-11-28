#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> ATAT "))
    print(
'''1.模块简介
----------
  该模块是PWmat和合金理论自动化工具包ATAT之间的接口。ATAT是一个泛称，指合金理论工具的集合，可用于生成特殊的准随机结构（SQS）、模拟无序固溶体、从第一原理构造簇经验、对晶格模型进行蒙特卡罗模拟以计算合金的热力学性质，团簇展开法...
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/pwmat_ATAT_interface_manual.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()