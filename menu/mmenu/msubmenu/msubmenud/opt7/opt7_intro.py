#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt7():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Anomalous Hall Conductivity (new interpolation method) "))
    print(
'''1.模块简介
----------
  本模块使用二阶插值方法计算反常霍尔电导。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_AHC.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt7()