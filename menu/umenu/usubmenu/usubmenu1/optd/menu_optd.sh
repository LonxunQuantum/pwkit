#!/bin/bash


usubmenu1::menu_optd() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/optd/optd_intro.py
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