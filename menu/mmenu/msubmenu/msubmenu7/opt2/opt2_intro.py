#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt2():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Absorption Spectrum Calculations for bulk systems using LDA+RPA, LDA+rt-TDDFT, HSE+rt-TDDFT methods "))
    print(
'''1.模块简介
----------
  本模块用于介绍如何使用LAD+RPA（随机相位近似）、LDA+rt-TDDFT和HSE（RSE）+rt-TDFT方法计算体系统的光学吸收光谱。PWmat可以使用HSE_α、HSE_ω、HSE_beta参数运行距离分离混合（RSH，在PWmat中也称为HSE）函数，这些参数表示短距离混合（HSE_β）和长距离混合（HSE_beta），以及过渡位置（HSE_omega，最佳调谐函数）。RSH可以用HSE_(周期性体系计算光吸收谱的几种方法，RPA/tddft/tddft+hse））
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_bulk_absorption_TDDFT.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt2()