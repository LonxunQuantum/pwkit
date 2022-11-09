#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt6():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> xsf2config.x "))
    print(
'''1.工具简介
----------
  用于将XSF文件转换为atom.config
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/xsfconfig.pdf
'''
    )

if __name__ == "__main__":
    opt6()