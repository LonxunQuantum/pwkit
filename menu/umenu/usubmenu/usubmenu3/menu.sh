#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt1.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt2.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt3.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt4.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt5.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt6.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt7.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt8.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt9.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opta.sh


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
        usubmenu3::opt1
        ;;
    2)
        usubmenu3::opt2
        ;;
    3)
        usubmenu3::opt3
        ;;
    4)
        usubmenu3::opt4
        ;;
    5)
        usubmenu3::opt5
        ;;
    6)
        usubmenu3::opt6
        ;;
    7)
        usubmenu3::opt7
        ;;
    8)
        usubmenu3::opt8
        ;;
    9)
        usubmenu3::opt9
        ;;
    a)
        usubmenu3::opta
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}