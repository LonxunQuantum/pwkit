import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 其他 "))
  print(
''' 暂时未开发更多 Module

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()