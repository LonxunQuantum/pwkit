#!/bin/bash


msubmenu8::menu_opt1() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/opt1/opt1_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenu8
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}