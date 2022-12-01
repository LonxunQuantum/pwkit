import click


@click.command()
def optb():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_TDDFT_rho.x "))
    print(
'''1.工具简介
----------
  用于输出TDDFT计算过程中某一时刻的激发电子和空穴的电荷密度
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_TDDFT_rho.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )

if __name__ == "__main__":
    optb()