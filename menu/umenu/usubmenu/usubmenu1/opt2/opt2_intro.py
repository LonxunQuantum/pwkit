#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> vwr2upf.x "))
    print(
'''1.工具简介
----------
  将vwr赝势转换为UPF赝势
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/vwr2upf.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()