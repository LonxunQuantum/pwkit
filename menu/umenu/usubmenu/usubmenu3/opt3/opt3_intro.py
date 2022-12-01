import click


@click.command()
def opt3():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> NAMD_psi.x "))
    print(
'''1.工具简介
----------
  用于查看NAMD计算中的波函数
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/NAMD_psi.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()