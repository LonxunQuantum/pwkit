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
    print("+{0:-^68}+".format(" KPoints Format "))
    print("\t* KPoints 的定义方式: ")
    print("\t\t1. KMesh (通过 etot.input 中的 MP_N123 定义)")
    print("\t\t2. 高对称点 (通过输入文件 IN.KPT 定义)")
        
    print("+{0:-^68}+".format("---------"))
    

if __name__ == "__main__":
    hsp_menu()