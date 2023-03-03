import os 
import click


@click.command()
def mmenu_cn():
    #print("{0:=^80}".format(" Module "))

    ### Part I. Utility 数据可视化
    print("{0:-^60}".format(" 态密度图绘制 "))
    print(
''' 1) 生成DOS.input文件    2) 总态密度     3) 投影态密度 (元素)      
 4) 投影态密度 (轨道)
'''
    )

    ### Part II. EXIT
    print(
'''
 bb) 返回上一级目录
 q)  退出'''
    )
    current_path = os.getcwd()
    dos_input_path = os.path.join(current_path, "DOS.input")
    if not os.path.exists(dos_input_path):
        print("+{0:-^78}+".format(" Warm Tips "))
        print("\033[0;32m   * 在绘制态密度之前, 需要先生成 DOS.input 文件! \033[0m")
        print('''   * 使用`echo -e 'u\\n3\\n1\\n1\\n0.04\\n4000\\n6,6,6\\n' | pwkit`生成默认的DOS.input''')
        print("+{0:-^78}+".format("---------"))
        #raise SystemExit

if __name__ == "__main__":
    mmenu_cn()