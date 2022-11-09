#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Berry Phase "))
    print(
'''1.模块简介
----------
  用现代极化理论计算离子钳位极化的方法(计算离子钳位极化）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_berryphase.pdf
'''
    )

if __name__ == "__main__":
    opt1()