#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^80}".format(" Module --> 	Wannier Band Interpolation "))
    print(
'''1.模块简介
----------
  Wannier Band Interpolation（WBI）是一种基于紧束缚近似和Wannieer函数的能带结构内插方法，
只需要少量的DFT计算，即可获得一些初始k点特征值。（基于紧束缚近似和瓦尼尔函数的插值方法，
利用少量密度泛函计算就可以扩展得到任意的K点特征值，可以高效计算能带）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Wannier_Band_Interpolation_manual.pdf
'''
    )

if __name__ == "__main__":
    opt4()