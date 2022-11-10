#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt5():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> ug_moment.x "))
    print(
'''1.工具简介
----------
  用于光学性质计算的角动量
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/%E8%AF%B4%E6%98%8E.pdf
'''
    )

if __name__ == "__main__":
    opt5()