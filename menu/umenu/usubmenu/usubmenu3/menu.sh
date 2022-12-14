#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
for i in {1,2,3,4,5,6,7,8,9,a}
    do 
        source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt${i}/menu_opt${i}.sh
    done


umenu::usubmenu3() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu
        ;;
    1)
        usubmenu3::menu_opt1
        exit 0
        ;;
    2)
        usubmenu3::menu_opt2
        exit 0
        ;;
    3)
        usubmenu3::menu_opt3
        exit 0
        ;;
    4)
        usubmenu3::menu_opt4
        exit 0
        ;;
    5)
        usubmenu3::menu_opt5
        exit 0
        ;;
    6)
        usubmenu3::menu_opt6
        exit 0
        ;;
    7)
        usubmenu3::menu_opt7
        exit 0
        ;;
    8)
        usubmenu3::menu_opt8
        exit 0
        ;;
    9)
        usubmenu3::menu_opt9
        exit 0
        ;;
    a)
        usubmenu3::menu_opta
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}