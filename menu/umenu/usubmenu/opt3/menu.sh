#!/bin/bash


umenu_usubmenu::opt3() {
while [ 1 ]
do
    $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt3/menu_cn.py
    read -p " ------------>>  
" submenuOpt
    case $submenuOpt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        umenu
        ;;
    1)
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt3/subopt3s/1.dos_input.py
        exit 0
        ;;
    2) 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt3/subopt3s/2.tdos_plot.py
        exit 0
        ;;
    3) 
        #$PYTHON_PATH
        exit 0
        ;;
    4) 
        #$PYTHON_PATH
        exit 0
        ;;
    esac
done
}