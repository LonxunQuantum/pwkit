import click


@click.command()
def opt3():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_rho.x "))
    print(
'''1.工具简介
----------
  将 pwscf 转换为 atom.config 格式的文件
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
    opt3()