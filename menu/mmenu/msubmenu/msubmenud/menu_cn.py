#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 输运性质 "))
  print(
''' 1) EMC
 2) Electrical conductivity
 3) Boltzwann
 4) BoltzTraP
 5) Anomalous Hall Conductivity（AHC）calculation
 6) pwmat_transport
 7) Anomalous Hall Conductivity（new interpolation method）
 8) NONEQUILIBRIUM_SCF
 9) Spin Hall Effect（SHC）

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()