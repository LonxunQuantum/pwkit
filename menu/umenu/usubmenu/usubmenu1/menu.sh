#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt1.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt2.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt3.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt4.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt5.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt6.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt7.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt8.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt9.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opta.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/optb.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/optc.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/optd.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opte.sh



umenu::usubmenu1() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/menu_cn.py
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
        usubmenu1::opt1
        ;;
    2)
        usubmenu1::opt2
        ;;
    3)
        usubmenu1::opt3
        ;;
    4)
        usubmenu1::opt4
        ;;
    5)
        usubmenu1::opt5
        ;;
    6)
        usubmenu1::opt6
        ;;
    7)
        usubmenu1::opt7
        ;;
    8)
        usubmenu1::opt8
        ;;
    9)
        usubmenu1::opt9
        ;;
    a)
        usubmenu1::opta
        ;;
    b)
        usubmenu1::optb
        ;;
    c)
        usubmenu1::optc
        ;;
    d)
        usubmenu1::optd
        ;;
    e)
        usubmenu1::opte
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}