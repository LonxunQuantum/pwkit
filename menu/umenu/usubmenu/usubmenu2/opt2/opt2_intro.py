#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
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
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()