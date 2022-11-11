#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt6():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Image charge interaction correction "))
    print(
'''1.模块简介
----------
  利用周期性的超胞计算带电缺陷是固态物理中的一类重要问题。然而，有限的超胞尺寸引起了长程图像电荷库仑相互作用。我们用缺陷屏蔽模型给出了image charge interaction的严格推导，其中可以避免使用体宏观介电常数(新的缺陷计算方法，解决超胞法中存在的长程库伦作用影响）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/ICIC_guide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    opt6()