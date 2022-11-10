#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt8():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_fatband_structure.x "))
    print(
'''1.工具简介
----------
  用于输出投影能带结构
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_fatband_structure.pdf
'''
    )

if __name__ == "__main__":
    opt8()