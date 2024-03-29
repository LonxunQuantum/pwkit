#!/bin/bash

# menu 显示函数 -- umenu_cn.py
source $PWKIT_ROOT/menu/umenu/usubmenu/opt3/menu.sh
source $PWKIT_ROOT/menu/umenu/usubmenu/opt4/menu.sh


umenu() {

while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/umenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
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
    3)  # 态密度绘制：tdos, pdos (原子), pdos (轨道)
        umenu_usubmenu::opt3
        exit
        ;;
    4) 
        #echo "能带图绘制"
        umenu_usubmenu::opt4
        exit
        ;;

    a)  
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opta/opta_use.py
        exit
        ;;
    b) 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/optb/optb_use.py
        exit
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}