#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Band alignment "))
    print(
'''1.模块简介
----------
  该模块用于计算能带对齐。能带对齐是半导体异质结研究中的一个重要参数，它与材料的许多特性直接相关，因此准确测量或计算该值具有重要意义。实验上，可以通过光电子光谱和光学方法测量能带对齐。然而，由于测量值与特定的生长环境有很大关系，例如晶格应变的大小，不同测量者的测试结果会有很大差异，无法直接比较。因此，从理论上计算半导体的能带对齐是非常重要的。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/band_alignment.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()