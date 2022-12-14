import click

@click.command()
def menu_cn():
    ### Part I. Generator
    print(
            "{0:=^90s}".format(" Generator ")
    )
    print(
''' g) 进入 Input Generator 模块''', end=''
    )
    print(
'''
 为 PWmat 生成输入文件。
'''        
    )

    ### Part II. Module
    print(
            "{0:=^90s}".format(" Module ")
    )
    print(
''' m) Module 功能简介''',
    )
    print(
''' 在PWmat的基础功能上, 我们针对用户的使用需求开发了一些顶层模块(MODULE)。
 这些MODULE中的一部分是与已有的优秀工具的接口, 一部分是以PWmat的计算结果为基础得
到实际需要的物理量, 一部分则是为特定的计算需求而设计的计算流程。这些MODULE涵盖了
物质结构, 基础性质, 针对大体系的计算以及机器学习力场等, 功能全面。
''')

    ### Part III. Utility
    print(
            "{0:=^90s}".format(" Utility ")
    )
    print(
''' u) 进入 Utility '''
    )
    print(
''' 为了方便用户进行计算的前、后处理, PWmat安装包内附带了一系列实用程序。通过这些程
序, 我们可以实现PWmat结构文件和其他常见晶体结构文件之间的相互转换、处理数据得到
可视化电荷密度、能带结构图、投影态密度、真空能级等操作。
'''
    )

    ### Part IV. Exit
    print(
''' q)  退出'''
    )
    

if __name__ == "__main__":
    menu_cn()