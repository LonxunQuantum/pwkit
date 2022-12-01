import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 极化性质 "))
  print(
''' 1) Defect Level
 2) Defect Nonradiative Decay
 3) Charge trapping calculation
 4) Charged defect calculation by TRSM
 5) anharmonic multi-phonon nonradiative transition
 6) Image charge interaction correction

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()