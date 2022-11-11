#!/bin/bash


msubmenud::menu_opt5() {
while [ 1 ]
    do 
        $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt5/opt5_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenud
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}