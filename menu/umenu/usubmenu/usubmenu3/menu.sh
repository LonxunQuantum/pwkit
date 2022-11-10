#!/bin/bash


# 加载 usubmenu 对应的所有opt函数


umenu::usubmenu3() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        umenu
        ;;
    1)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt1.py
        exit 0
        ;;
    2)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt2.py
        exit 0
        ;;
    3)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt3.py
        exit 0
        ;;
    4)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt4.py
        exit 0
        ;;
    5)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt5.py
        exit 0
        ;;
    6)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt6.py
        exit 0
        ;;
    7)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt7.py
        exit 0
        ;;
    8)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt8.py
        exit 0
        ;;
    9)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt9.py
        exit 0
        ;;
    a)
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opta.py
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}