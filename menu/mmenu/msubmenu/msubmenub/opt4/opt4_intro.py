#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Charged defect calculation by TRSM "))
    print(
'''1.模块简介
----------
  本模块介绍了如何通过转移到实态模型（TRSM）计算三维体和低维半导体中带电缺陷的形成能量，该模型可以克服概念模糊性和计算困难，特别是对于由“凝胶模型”引起的低维半导体材料(计算低维结构的带电缺陷，解决传统凝胶模型算低维缺陷能量发散问题）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Charged%20defect%20calculation-module.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt4()