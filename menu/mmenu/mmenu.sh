#!/bin/bash

# 加载menu函数
source $PWKIT_ROOT/menu.sh

# 加载mmenu显示函数
source $PWKIT_ROOT/menu/mmenu/mmenu_cn.sh
source $PWKIT_ROOT/menu/mmenu/mmenu_en.sh

# 加载1msubmenu显示函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/menu.sh

mmenu() {

while [ 1 ]
    do
        mmenu::mmenu_${glanguage}
        read -p " ------------>> " menuOpt
    
    case $menuOpt in
    q|Q)
        exit
        ;;
    b|B)
        menu
        ;;
    1)
        mmenu::1    # 结构搜索
        ;;
    2) 
        exit            # 无序结构
        ;;
    3)
        exit            # 分子动力学数据处理
        ;;

    esac
    done
}