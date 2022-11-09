#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^80}".format(" Module --> Absorption Spectrum for non-periodic systems "))
    print(
'''1.模块简介
----------
  该模块用于通过rt-TDFT方法计算光学吸收光谱，它仅适用于非周期系统，如团簇或分子。
关于周期性系统，请参阅模块18和模块38(通过rt-tdft计算非周期体系的光吸收谱，周期性
体系参看模块18和38）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/plot_tddft_absorp_guide.pdf
'''
    )

if __name__ == "__main__":
    opt1()