#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 结构搜索 "))
  print(
''' 1) CALYPSO
 2) USPEX
 3) Genetic algorithm to search global minimum structure

 bb) 返回上一级目录
 q)  退出
'''
  )

if __name__ == "__main__":
  menu_cn()