#!/bin/bash


msubmenuh::menu_opt1() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/opt1/opt1_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenuh
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}