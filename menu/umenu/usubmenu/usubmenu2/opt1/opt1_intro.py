import click


@click.command()
def opt1():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_band_structure.x "))
    print(
'''1.工具简介
----------
  用于画能带
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_band_structure.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt1()