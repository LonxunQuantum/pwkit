#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 超快动力学 "))
  print(
''' 1) TDDFT Carrier Cooling
 2) Boltzman-NAMD
 3) Ion collision simulation by rt-TDDFT

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()