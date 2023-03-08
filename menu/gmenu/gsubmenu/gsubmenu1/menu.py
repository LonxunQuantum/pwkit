import os
import sys
import signal
import shutil
from menu_cn import mmenu_cn


from menu_utilitys import *


def generate_etot_input():
    ### Step 1. 如果存在 `etot.input` 和 `IN.SOLVENT` 文件，则先将其删除
    current_path = os.getcwd()
    if os.path.exists( os.path.join(current_path, "etot.input") ):
        shutil.rmtree( os.path.join(current_path, "etot.input") )
    if os.path.exists( os.path.join(current_path, "IN.SOLVENT") ):
        shutil.rmtree( os.path.join(current_path, "IN.SOLVENT") )
    
    
    ### Step 2. 根据 `input_from_terminal`
    while (True):
        mmenu_cn()  # 显示生成 etot.input 的菜单
        input_from_terminal = input(" ------------>>\n")
        
        if input_from_terminal.upper() in ['q', 'Q']:
            ### Note: 直接退出 `父进程`，并在 Terminal 输出 `Terminated`
            os.kill(os.getppid(), 9)
        elif input_from_terminal.upper() in ['bb', 'BB']:
            p2 = subprocess.Popen(
                    ['$PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/execute_gmenu.sh'],
                    stdout=subprocess.PIPE,
                    shell=True,
            )
            p2.wait()


if __name__ == "__main__":
    generate_etot_input()