#!/bin/bash

# 加载menu函数 -- gmenu_cn.py

## 加载 usubmenu 函数
# 1. 格式转换
source $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/menu_test.sh
source $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/menu.sh
source $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu3/opt1/opt1.sh
#source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu4/menu.sh


gmenu() {

while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gmenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    1)
        gmenu::gsubmenu1
        #$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/menu.py
        ;;
    2)
        gmenu::gsubmenu2
        ;;
    3)  # 生成高对称点的文件：只有一个选项
        gsubmenu3::opt1
        exit
        ;;
    4)
        #umenu::usubmenu4
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu4/opt1.py
        exit
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}