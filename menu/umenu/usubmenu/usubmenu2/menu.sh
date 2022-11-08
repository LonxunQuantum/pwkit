#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt1.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt2.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt3.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt4.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt5.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt6.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt7.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt8.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt9.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opta.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/optb.sh



umenu::usubmenu2() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/menu_cn.py
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
        usubmenu2::opt1
        ;;
    2)
        usubmenu2::opt2
        ;;
    3)
        usubmenu2::opt3
        ;;
    4)
        usubmenu2::opt4
        ;;
    5)
        usubmenu2::opt5
        ;;
    6)
        usubmenu2::opt6
        ;;
    7)
        usubmenu2::opt7
        ;;
    8)
        usubmenu2::opt8
        ;;
    9)
        usubmenu2::opt9
        ;;
    a)
        usubmenu2::opta
        ;;
    b)
        usubmenu2::optb
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}