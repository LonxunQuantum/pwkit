#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opt5():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> Raman "))
    print(
'''1.模块简介
----------
  拉曼光谱是一种用于材料表征的强大的非侵入性技术，它独特地提取了关于局部环境中振动和化学性质、不均匀性、应变、结晶度、电子-声子耦合和非谐性的信息。这里我们可以获得高斯展宽的拉曼光谱(非共振拉曼）。
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/guide_Raman.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt5()