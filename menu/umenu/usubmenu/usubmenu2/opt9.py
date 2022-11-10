#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt9():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_electrical_conductivity.x "))
    print(
'''1.工具简介
----------
  用于输入电导率
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_electrical_conductivity.pdf
'''
    )

if __name__ == "__main__":
    opt9()