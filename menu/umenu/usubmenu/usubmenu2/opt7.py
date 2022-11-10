#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt7():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_TDDFT.x "))
    print(
'''1.工具简介
----------
  用于画RT-TDDFT的输出图像
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_TDDFT.pdf
'''
    )

if __name__ == "__main__":
    opt7()