#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Born effective charge "))
    print(
'''1.模块简介
----------
  玻恩有效电荷是在零外场条件下，由i方向的原子位移引起的j方向宏观极化变化之间的比例系数，它量化了光学声子和电场之间的耦合。在本模块中，我们使用贝里相方法计算出生电荷(用贝里相位方法计算天生有效电荷）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/borncharge_guide.pdf
'''
    )

if __name__ == "__main__":
    opt2()