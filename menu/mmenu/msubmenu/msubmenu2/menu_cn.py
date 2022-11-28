#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 无序结构 "))
  print(
''' 1) ATAT
 2) disorder
 3) Virtual Crystal Approximation (VCA) Calculations

 bb)  返回上一级目录
 q)   退出
'''
)


if __name__ == "__main__":
  menu_cn()