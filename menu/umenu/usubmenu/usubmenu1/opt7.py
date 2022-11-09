#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt7():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> pwscf2config.x "))
    print(
'''1.工具简介
----------
  用于将pwscf输入文件转换为atom.config
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/pwscf2config.pdf
'''
    )

if __name__ == "__main__":
    opt7()