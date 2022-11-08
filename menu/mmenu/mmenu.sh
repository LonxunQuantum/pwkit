#!/bin/bash

# 加载mmenu显示函数: mmenu_cn.py, mmenu_en.py

# 加载1msubmenu显示函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu.sh

mmenu() {

while [ 1 ]
    do
        $PWKIT_ROOT/menu/mmenu/mmenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
        exit
        ;;
    b|B)
        menu
        ;;
    1)
        mmenu::msubmenu1    # 结构搜索
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