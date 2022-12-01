import click


@click.command()
def opt6():
    ### Part I. 模块名
    print("{0:=^180}".format(" Module --> High accurate k-point interpolation scheme "))
    print(
'''1.模块简介
----------
  本模块介绍一种新的二阶k点插值方案。它可以用于绘制带结构。但它也可以用于在布里渊区上进行其他k点积分方案。与以前的interp_absrption和interp_DOS方法相比，这一方法更准确。但它代价也更大。未来可能需要使用GPU进行改进。它可以用于任何哈密顿量，例如DFT+U或HSE等(一种新的二阶插值方法，与之前的方法相比，这种插值方法更精确，适用范围更广，计算量也更大）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:3389/pwmat-resource/module-download7/pdf/interpolation_2nd.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt6()