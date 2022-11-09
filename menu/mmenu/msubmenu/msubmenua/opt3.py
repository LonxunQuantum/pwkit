#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Piezoelectric tensor "))
    print(
'''1.模块简介
----------
  压电材料在施加外部宏观应变时表现出诱导的电极化。可以将该模块与模块42和43一起用于计算(计算电极化强度，电偶极矩）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Piezo_guide.pdf
'''
    )

if __name__ == "__main__":
    opt3()