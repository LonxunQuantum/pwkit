#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt7():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> bandgap "))
    print(
'''1.工具简介
----------
  从REPORT中直接读取能带带隙
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/bandgap.pdf
'''
    )

if __name__ == "__main__":
    opt7()