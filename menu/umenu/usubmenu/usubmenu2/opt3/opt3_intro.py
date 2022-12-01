import click


@click.command()
def opt3():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> absorption_spec_K2step.x "))
    print(
'''1.工具简介
----------
  用于RT-TDDFT体相结构光谱画图
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/absorption_spec_K.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt3()