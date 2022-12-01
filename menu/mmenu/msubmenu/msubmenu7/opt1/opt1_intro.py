import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Absorption Spectrum for non-periodic systems "))
    print(
'''1.模块简介
----------
  该模块用于通过rt-TDFT方法计算光学吸收光谱，它仅适用于非周期系统，如团簇或分子。关于周期性系统，请参阅模块18和模块38(通过rt-tdft计算非周期体系的光吸收谱，周期性体系参看模块18和38）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/plot_tddft_absorp_guide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()