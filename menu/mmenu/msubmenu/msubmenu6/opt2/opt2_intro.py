import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> High temperature phonon calculation "))
    print(
'''1.模块简介
----------
  不稳定结构的高温非谐声子模式（计算有限温度的声子谱）。
'''
    )
    print(
'''2.使用手册
----------
http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/High_T_phonon.pdf
'''
    )    
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt2()