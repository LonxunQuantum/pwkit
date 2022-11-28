#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt7():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> TDDFT absorption spectrum(Linear response)"))
    print(
'''1.模块简介
----------
  该代码使用微扰理论（线性响应）来求解Casenda方程（或其HSE对应部分），以计算小分子的吸收光谱（在盒子中计算）。这可以与实时TDDFT吸收光谱计算进行比较。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/tddft_lr_absorp.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt7()