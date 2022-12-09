import click



@click.command()
def hsp_menu():
    '''
    Description
    -----------
        1. 当进行NS(非自洽计算)时，需要选择按照 MP_N123 或者 IN.KPT 文件
            - MP_N123 参数: 储存了KMesh, e.g. "8 8 8"
            - IN.KPT 文件: 储存了高对称点信息
    '''
    print("")