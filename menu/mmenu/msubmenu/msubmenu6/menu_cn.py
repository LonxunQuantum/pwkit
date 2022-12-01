import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 声子计算 "))
  print(
''' 1) PyPWmat
 2) High temperature phonon calculation
 3) PWphono3py
 4) electron-phonon coupling (EPC)

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()
