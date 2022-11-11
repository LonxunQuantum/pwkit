#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> gilbert damping constant "))
    print(
'''1.模块简介
----------
  该模块用于计算体吉尔伯特阻尼常数，该常数描述了Landau-Lifshitz-Gilbert（LLG）方程中磁矩的阻尼项。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/gilbert_damping_constant.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()