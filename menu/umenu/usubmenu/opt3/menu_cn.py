import os 
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. Utility 数据可视化
    print("{0:-^60}".format(" 态密度图绘制 "))
    print(
''' 1) 生成DOS.input文件    2) 总态密度     3) 投影态密度 (元素)      
 4) 投影态密度 (轨道)
'''
    )

    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    print("\033[0;31m Warm Tips: 在绘制态密度之前, 最好先生成 DOS.input 文件! \033[0m")

if __name__ == "__main__":
    mmenu_cn()