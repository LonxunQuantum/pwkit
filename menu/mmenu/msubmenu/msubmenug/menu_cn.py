import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 电子束辐照分解 "))
  print(
''' 1) TDDFT Carrier Cooling
 2) Auger Decay Rate calculation
 3) Cross Section calculation

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()