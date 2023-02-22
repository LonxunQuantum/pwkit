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
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt3/opt3_use.py
        exit
        ;;
    4) 
        #echo "能带图绘制"
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt4/opt4_use.py
        exit
        ;;
    5) 
        echo "投影能带"
        exit
        ;;

    a)  
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opta/opta_use.py
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