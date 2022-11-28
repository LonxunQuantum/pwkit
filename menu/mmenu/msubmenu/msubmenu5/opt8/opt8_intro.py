#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def opt8():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Electron localization function（ELF） "))
    print(
'''1.模块简介
----------
  电子局域函数（Electron Localization Function—ELF）是研究电子结构的手段之一。用来描述以某个位置处的电子为参考，在其附近找到与他同自旋的电子的概率，可以表征这个作为参考的电子的局域化程度，也是一种描述在多电子体系中的电子对概率的方法。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/ELF.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt8()