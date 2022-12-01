import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 大体系计算 "))
  print(
''' 1) Charge Patching Method
 2) Charge Patching Method introduction (CPM)
 3) MLFF

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()