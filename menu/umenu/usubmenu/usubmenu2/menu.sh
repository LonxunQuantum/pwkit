#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
for i in {1,2,3,4,5,6,7,8,9,a,b}
    do 
        source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/opt${i}/menu_opt${i}.sh
    done


umenu::usubmenu2() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu2/menu_cn.py
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
        usubmenu2::menu_opt1
        exit 0
        ;;
    2)
        usubmenu2::menu_opt2
        exit 0
        ;;
    3)
        usubmenu2::menu_opt3
        exit 0
        ;;
    4)
        usubmenu2::menu_opt4
        exit 0
        ;;
    5)
        usubmenu2::menu_opt5
        exit 0
        ;;
    6)
        usubmenu2::menu_opt6
        exit 0
        ;;
    7)
        usubmenu2::menu_opt7
        exit 0
        ;;
    8)
        usubmenu2::menu_opt8
        exit 0
        ;;
    9)
        usubmenu2::menu_opt9
        exit 0
        ;;
    a)
        usubmenu2::menu_opta
        exit 0
        ;;
    b)
        usubmenu2::menu_optb
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}