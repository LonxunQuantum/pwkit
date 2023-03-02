import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. Utility 数据可视化
    print("{0:-^60}".format(" 数据可视化 "))
    print(
''' 1) 电荷密度可视化        2) 波函数可视化        3) 态密度图绘制
 4) 能带图绘制            5) 投影能带 (待开发)      
'''
    )

    ### Part II. Utility 数据后处理
    print("{0:-^60}".format(" 数据后处理 "))
    print(
''' a) 能带带隙              b) 真空能级 (待开发)
'''
    )


    ### Part V. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )


if __name__ == "__main__":
    mmenu_cn()