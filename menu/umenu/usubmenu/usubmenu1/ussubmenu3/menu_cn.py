import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^60}".format(" 查看结构信息 "))
    print(
''' 1) 查看原晶胞的基矢
 2) 查看原晶胞的基矢长度
 3) 查看原晶胞的基矢间夹角
 4) 查看倒易点阵的基矢 (单位: 2pi/埃)
 5) 查看倒易点阵的基矢长度 (单位: 2pi/埃)
 6) 查看晶胞的对称性信息
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