#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> 	magnetic exchange parameters "))
    print(
'''1.模块简介
----------
  本模块介绍了计算磁交换参数的four state method。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/four_states_method.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()