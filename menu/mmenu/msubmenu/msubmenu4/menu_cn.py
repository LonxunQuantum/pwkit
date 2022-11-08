#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> CIF 文件转换与结构处理 "))
  print(
''' 1) CIF2CELL
 2) CELL2

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()