#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> uspp2upf.x "))
    print(
'''1.工具简介
----------
  将uspp赝势转换为UPF赝势
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/uspp2upf.pdf
'''
    )

if __name__ == "__main__":
    opt3()