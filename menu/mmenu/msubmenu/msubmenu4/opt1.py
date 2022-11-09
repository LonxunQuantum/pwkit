#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> CIF2CELL "))
    print(
'''1.模块简介
----------
  该模块是PWmat和CIF2CELL之间的接口。CIF2CELL是一种工具，用于从CIF文件生成各种电子结构代码的结构文件。该程序目前支持许多流行的电子结构程序的输出，包括PWmat、ABINIT、ASE、CASTEP、CP2K、CPMD、CRYSTAL09、Elk、EMTO、Exciting、Fleur、FHI aims、Hutsepot、MOPAC、Quantum Espresso、RSPt、Siesta、SPR-KKR、VASP。还导出一些相关格式，如.coo、.cfg和.xyz文件(将到cif文件转换为atom.config））
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/CIF2CELL.pdf
'''
    )

if __name__ == "__main__":
    opt1()