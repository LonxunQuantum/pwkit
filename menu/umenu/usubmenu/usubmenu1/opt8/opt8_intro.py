import click


@click.command()
def opt8():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_from_config.x "))
    print(
'''1.工具简介
----------
  用于将atom.config转换为xsf和xyz格式的文件
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/convert_from_config.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt8()