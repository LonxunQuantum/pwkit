import click


@click.command()
def opta():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> use charge density to calculate absorption spectrum for large-scale insulating systems "))
    print(
'''1.模块简介
----------
  该方法使用随机波函数计算光学吸收光谱的数千个Chebyshev moments，并将这些moments转换回能量空间。结果与大型绝缘系统的直接计算结果很好地比较。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Use_charge_density_to_calculate_absorption_spectrum_of_large_quantum.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opta()