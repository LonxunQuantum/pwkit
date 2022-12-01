import click


@click.command()
def opta():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> upf2upfSO.x "))
    print(
'''1.工具简介
----------
  用于将pwscf的含有spin-orbital的赝势转换为PWmat专有数据格式的赝势
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/upf2upfSO.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opta()