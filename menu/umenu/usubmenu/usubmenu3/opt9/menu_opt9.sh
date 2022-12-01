#!/bin/bash


usubmenu3::menu_opt9() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt9/opt9_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu::usubmenu3
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}