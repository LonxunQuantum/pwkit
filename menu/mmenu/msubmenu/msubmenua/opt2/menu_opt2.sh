#!/bin/bash


msubmenua::menu_opt2() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt2/opt2_intro.py
        read -p " ------------>>  
" opt
    case $opt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        mmenu::msubmenua
        ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    esac
    done
}