#!/bin/bash


usubmenu3::menu_opt4() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/opt4/opt4_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
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