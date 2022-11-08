#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 电子结构 "))
  print(
''' 1) Band alignment                     2) BANDUP
 3) PDOS & fatband structure           4) Wannier Band Interpolation
 5) U value calculation in LDA+U       6) High accurate k-point interpolation scheme
 7) Band structure calculation by WKM  8) Electron localization function（ELF）

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()