#!/bin/bash

# menu 显示函数 -- umenu_cn.py


umenu() {

while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/umenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit
        ;;
    bb|BB)
        menu
        ;;
    1)
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt1/opt1_use.py
        exit
        ;;
    2) 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt2/opt2_use.py
        exit
        ;;
    3) 
        echo "请输入绘制的能量范围 (e.g. -5,5)"
        read -p " ------------>>
" range_energy
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt3/opt3_use.py $range_energy
        exit
        ;;
    4) 
        echo "态密度图绘制"
        exit
        ;;
    5) 
        echo "投影能带"
        exit
        ;;

    a)  
        echo "能带带隙"
        exit
        ;;
    b) 
        echo "真空能级"
        exit
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}