#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 物质结构
    print("{0:-^60}".format(" 物质结构 "))
    print(
''' 1) 结构搜索                2) 无序结构
 3) 分子动力学数据处理      4) CIF 文件转换与结构处理
'''
    )

    ### Part II. 电子结构及声子计算
    print("{0:-^55}".format(" 电子结构及声子计算 "))
    print(
''' 5) 电子结构                6) 声子计算
'''
    )

    ### Part III. 电子结构及声子计算
    print("{0:-^53}".format(" 光、磁、力学和极化性质 "))
    print(
''' 7) 光学性质                8) 磁学性质
 9) 力学性质                a) 极化性质
'''
    )

    ### Part IV. 其他模块
    print("{0:-^60}".format(" 其他模块 "))
    print(
''' b) 缺陷性质                c) 电化学性质
 d) 输运性质                e) 超快动力学过程
 f) Beyond DFT              g) 电子束辐照分解
 h) 大体系计算              i) 机器学习力场
 j) 其它
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