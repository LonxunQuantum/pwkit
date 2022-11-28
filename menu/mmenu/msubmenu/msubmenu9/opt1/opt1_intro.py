#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt1():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> ELPWmat "))
    print(
'''1.模块简介
----------
  该模块用于通过高通量法计算弹性常数。ELPWmat是一个高效的开源python程序，使用PWmat通过高通量第一原理计算来计算三维材料和二维材料的弹性常数、柔度常数、杨氏模量、剪切模量和体积模量以及泊松比。对于3D材料，根据Voigt-Reuss-Hill近似，ELPWmat可以计算弹性常数、柔度常数、多晶杨氏模量、剪切模量和体积模量以及泊松比。对于二维材料，ELPWmat可以计算弹性常数、柔度常数、平面内杨氏模量、剪切模量和平面内泊松比。（计算三维材料和二维材料的弹性常数，顺应常数，杨氏，剪切模量和体积模量以及泊松比））。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/four_states_method.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt1()