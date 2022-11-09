#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def optd():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_wg2rho "))
    print(
'''1.工具简介
----------
  将某个或者多个波函数转化成电荷密度
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/convert_wg2rho.pdf
'''
    )

if __name__ == "__main__":
    optd()