#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_DOS.py "))
    print(
'''1.工具简介
----------
  用于画态密度
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_DOS.pdf
'''
    )

if __name__ == "__main__":
    opt2()