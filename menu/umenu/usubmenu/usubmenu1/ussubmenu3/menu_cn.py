import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 格式转换
    print("{0:-^70}".format(" 查看结构信息 "))
    print(
''' 1) 查看原晶胞的基矢\t\t\t2) 查看原晶胞的基矢长度
 3) 查看原晶胞的基矢间夹角\t\t4) 查看倒易点阵的基矢 (单位: 2pi/埃)
 5) 查看倒易点阵的基矢长度 (单位: 2pi/埃)
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