import click


@click.command()
def opt9():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_tddft_absorp.x "))
    print(
'''1.工具简介
----------
  主要用于PWmat RT-TDDFT 画光吸收谱
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_tddft_absorp_guide.pdf
'''
    )
    print(
''' bb) 返回上一级目录
 q)  退出'''
    )
    

if __name__ == "__main__":
    opt9()