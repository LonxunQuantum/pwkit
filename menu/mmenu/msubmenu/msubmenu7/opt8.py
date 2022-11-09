#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt8():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> second harmonic generation (SHG) "))
    print(
'''1.模块简介
----------
  本模块描述了一种使用RPA方法计算体系统二阶磁化率的方法，我们使用二阶插值方法。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/RPA_shg_20220418.pdf
'''
    )

if __name__ == "__main__":
    opt8()