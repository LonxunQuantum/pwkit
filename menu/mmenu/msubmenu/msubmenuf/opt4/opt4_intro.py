#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt4():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> RPA_correlation_energy "))
    print(
'''1.模块简介
----------
  相关能量Ec被定义为Hartree-Fock能量Ex相对于总能量的缺失部分，即Etot＝Ex+Ec。随机相位近似（RPA）是提供对Ec的访问的这种近似。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/RPAcorrEn.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt4()