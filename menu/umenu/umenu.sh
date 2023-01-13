#!/bin/bash

# 加载menu函数 -- umenu_cn.py

## 加载 usubmenu 函数
# 1. 格式转换
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/menu.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/menu.sh
#source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/menu.sh
#source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu4/menu.sh


umenu() {

while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/umenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit
        ;;
    bb|BB)
        menu
        ;;
    1)
        umenu::usubmenu1
        ;;
    2) 
        umenu::usubmenu2
        ;;
    3) 
        umenu::usubmenu3
        ;;
    4) 
        umenu::usubmenu4
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}