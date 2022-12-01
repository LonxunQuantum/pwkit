import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Charge Patching Method "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用电荷修补方  行直接密度泛函理论（DFT）计算，并将其电荷密度分解为分配给每个原子的电荷基序。然后通过重新组合电荷基序来构建感兴趣的大系统的总电荷密度，并用于生成DFT哈密顿量。已经表明，CPM给出了与直接从头计算几乎相同的结果。（使用CPM方法计算大体系，比如量子点、磨角石墨烯）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/Charge_patching_Manual.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()