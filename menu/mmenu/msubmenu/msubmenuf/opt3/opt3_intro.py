#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt3():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> PWmat_BSE "))
    print(
'''1.模块简介
----------
  Bethe-Salpeter方程可用于描述光吸收光谱和束缚激子波函数的电子-空穴相互作用（PWmat自己的BSE模块，与yambo相比，后续可以有更灵活的开发）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/PWmat_BSE_Guide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt3()