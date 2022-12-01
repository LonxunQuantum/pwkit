import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 磁学性质 "))
  print(
''' 1) gilbert damping constant
 2) Heisenberg exchange interaction constant
 3) magnetic exchange parameters

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()