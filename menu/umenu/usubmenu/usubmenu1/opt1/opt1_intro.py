#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> convert_rho.x "))
    print(
'''1.工具简介
----------
  将OUT.VR、OUT.RHO转换为RHO.XSF格式
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/convert_rho.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()