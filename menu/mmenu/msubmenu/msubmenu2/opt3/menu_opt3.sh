#!/bin/bash


msubmenu2::menu_opt3() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu2/opt3/opt3_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenu2
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}