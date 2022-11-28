#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt9():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> infrared spectrum/born charge(finite electric field method) "))
    print(
'''1.模块简介
----------
  区别于module 43，利用finite electric field方法求得born charge，并得到红外光谱。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_infrared_20211202.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt9()