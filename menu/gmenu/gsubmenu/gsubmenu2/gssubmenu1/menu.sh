#!/bin/bash


### 加载 usubmenu 对应的所有opt函数: 直接调用 Python 脚本，不需要 source `shell函数`


gsubmenu2::gssubmenu1() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        conda deactivate
        exit 0
        ;;
    bb|BB)
        gmenu::gsubmenu2
        ;;
    1)  
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt1/opt1_use.py     
        exit 0
        ;;
    2)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt2/opt2_use.py
        exit 0
        ;;
    3)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt3/opt3_use.py
        exit 0
        ;;
    4)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt4/opt4_use.py
        exit 0
        ;;
    5)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt5/opt5_use.py
        exit 0
        ;;
    6)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt6/opt6_use.py
        exit 0
        ;;
    7)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt7/opt7_use.py
        exit 0
        ;;
    8)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt8/opt8_use.py
        exit 0
        ;;
    9)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu1/opt9/opt9_use.py
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}