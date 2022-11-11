#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt8():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> nonradiative.x "))
    print(
'''1.工具简介
----------
  求非辐射衰减系数
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/nonradiative.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt8()