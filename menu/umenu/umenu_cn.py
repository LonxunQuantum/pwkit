import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 物质结构
    print("{0:-^60}".format(" 格式转换 "))
    print(
''' 1) 结构转换            2) 电荷密度转换
 3) 电势转换            4) 波函数转换        
'''
    )

    ### Part II. 电子结构及声子计算
    print("{0:-^59}".format(" 数据可视化 "))
    print(
''' 待开发...
'''
    )

    ### Part III. 电子结构及声子计算
    print("{0:-^59}".format(" 数据后处理 "))
    print(
''' 待开发...
'''
    )


    ### Part V. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出
'''
    )


if __name__ == "__main__":
    mmenu_cn()