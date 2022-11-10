#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click


@click.command()
def opta():
    ### Part I. Utility 名
    print("{0:=^180}".format(" Utility --> plot_TDDFT_allk.x "))
    print(
'''1.工具简介
----------
  用于输出TDDFT计算过程中指定能带范围（所有k点）的电子数随时间的变化。（如统计激发电子数随时间变化）
'''
    )
    print(
'''2.使用手册
----------
  http://www.pwmat.com:8080/upload/utility/pdf/plot_TDDFT_allk.pdf
'''
    )

if __name__ == "__main__":
    opta()