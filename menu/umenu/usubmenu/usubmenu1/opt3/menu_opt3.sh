#!/bin/bash


usubmenu1::menu_opt3() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/opt3/opt3_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        umenu::usubmenu1
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}