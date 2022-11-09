#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt6():
    ### Part I. 模块名
    print("{0:=^80}".format(" Module --> Absorption coefficient/Extinction coefficient/Reflectivity/Refractive index/Emissivity calculations "))
    print(
'''1.模块简介
----------
  使用RPA方法计算各种光学性质，如吸收系数/消光系数/反射率/折射率/发射率等。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_emissivity.pdf
'''
    )

if __name__ == "__main__":
    opt6()