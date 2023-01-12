import click


@click.command()
def optc():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_realwg.x "))
    print(
'''1.工具简介
----------
  将波函数转化到实空间，然后用VESTA可以查看
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/convert_reawg.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    optc()