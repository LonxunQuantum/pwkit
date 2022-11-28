#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. 任务类型
    print("{0:-^75}".format(" 任务类型 "))
    print(
''' SC) 自洽计算              CR) 晶格+原子位置优化      AR) 固定晶格优化原子位置
 NS) 非自洽计算            DS) 原子轨道投影（态密度） OS) 振子强度计算
 EP) 电子声子耦合系数计算  MD) 从头算分子动力学       NA) 非绝热分子动力学 
 TD) 含时密度泛函计算      TC) 过渡态计算             TS) 过渡态搜索
'''
    )

    ### Part II. 泛函设置
    print("{0:-^75}".format(" 泛函设置 "))
    print(
''' PE) PBE(默认)    91) PW91     PS) PBEsol      LD) CA-PZ       H6) HSE06
 H3) HSE03        P0) PBE0     B3) B3LYP       TP) TPSS        SC) SCAN
'''
    )

    ### Part III. 赝势设置
    print("{0:-^75}".format(" 赝势设置 "))
    print(
''' SG) SG15(默认)   PD) PD04      FH) FHI        PW) PWM         UD) 自定义
'''
    )

    ### Part IV. 特殊设置
    print("{0:-^75}".format(" 特殊设置 "))
    print(
''' 
 SP) 自旋极化    SO) 自旋轨道耦合   SN) 非共线磁矩+自旋轨道耦合    CS) 带电体系
 PU) DFT+U       D3) DFT-D3         FF) 固定电势计算               SE) 溶剂效应
'''
    )

    ### Part V. 输入示例
    print("{0:-^75}".format(" 输入示例 "))
    print(
''' SCH6        CRSPCS
'''
    )

    ### Part VI. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出
'''
    )


if __name__ == "__main__":
    mmenu_cn()