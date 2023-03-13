import os 
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. Utility 数据可视化
    print("{0:-^60}".format(" 能带图绘制 "))
    print(
''' 1) 总能带       2) 投影能带 (元素)       3) 投影能带 (轨道)     
'''
    )

    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    mmenu_cn()