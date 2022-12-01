import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Absorption Spectrum and dielectric constant Calculations for bulk systems using RPA method "))
    print(
'''1.模块简介
----------
  RPA方法（二阶插值）计算体材料或二维材料高频介电函数（电子部分贡献），同时给出折射率、反射率、吸收系数等结果。另外可以给出考虑局域场效应时的宏观介电常数。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_RPA_absorb_20220401.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt3()