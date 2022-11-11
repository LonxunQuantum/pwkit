#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def optb():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> atominfo.x "))
    print(
'''1.工具简介
----------
  用于给出atom.config中的结构信息
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/atominfo.pdf
'''
    )    
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    optb()