#!/bin/bash


### 加载 usubmenu 对应的所有opt函数: 直接调用Python脚本，不需要 source `shell 函数`


gsubmenu2::gssubmenu2() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu2/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        gmenu::gsubmenu2
        ;;
    1)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu2/opt1/opt1_use.py
        exit 0
        ;;
    2)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu2/opt2/opt2_use.py
        exit 0
        ;;
    3)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu2/opt3/opt3_use.py
        exit 0
        ;;
    4)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu2/opt4/opt4_use.py
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}