import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 物质结构
    print("{0:-^60}".format(" 生成输入文件 "))
    print(
''' 1) 生成etot.input                2) 结构文件格式转换
 3) 生成高对称点文件              4) 外加电场
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