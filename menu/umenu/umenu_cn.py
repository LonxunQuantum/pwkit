#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^50}".format(" Utility"))
    print(
''' 1) 格式转换      2) 数据可视化      
 3) 数据后处理    4) 其它
'''
    )

    ### Part II. EXIT
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )


if __name__ == "__main__":
    mmenu_cn()