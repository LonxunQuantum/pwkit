import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 超快动力学 "))
  print(
''' 1) YAMBO
 2) BSE-YAMBO
 3) PWmat_BSE
 4) RPA_correlation_energy

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()