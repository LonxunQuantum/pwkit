import click


@click.command()
def opt6():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_rho.x "))
    print(
'''1.工具简介
----------
  用于将cif文件转换为atom.config
'''
    )
    print(
'''2.使用手册
----------
  
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt6()