#!/bin/bash


msubmenu7::menu_opt7() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt7/opt7_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenu7
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}