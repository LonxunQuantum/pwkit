import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 极化性质 "))
  print(
''' 1) Berry Phase
 2) Born effective charge
 3) Piezoelectric tensor
 4) ionic dieclectric contribution

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()