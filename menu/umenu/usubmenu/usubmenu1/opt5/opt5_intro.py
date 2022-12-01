import click


@click.command()
def opt5():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> cell2config.x "))
    print(
'''1.工具简介
----------
  用于将CASTEP的CELL文件转换为atom.config
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/cell2config.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt5()