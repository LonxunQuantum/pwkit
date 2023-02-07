#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
for i in {1,2,3}
    do  
        source $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu${i}/menu.sh
    done


gmenu::gsubmenu2() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/menu_cn.py
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
        gsubmenu2::gssubmenu1
        exit 0
        ;;
    2)
        gsubmenu2::gssubmenu2
        exit 0
        ;;
    3)
        gsubmenu2::gssubmenu3
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}