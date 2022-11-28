#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> MLFF "))
    print(
'''1.模块简介
----------
  机器学习力场（MLFF）平台旨在生成精度与Ab Initio DFT分子动力学相当的力场。它提供了8种具有平移、旋转和置换不变性的特征。它还支持4个用于训练和预测的引擎，分别是：1. Linear Model 2. Nonlinear VV Model 3. Kalman Filter-based Neural Netowrk (KFNN) 4. Kalman Filter-based Deep Potential Model(KFDP)。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/mlff_manual.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()