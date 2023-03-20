#!/bin/bash


umenu_usubmenu::opt4() {
while [ 1 ]
do
    $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt4/menu_cn.py
    #if [ ! -f "DOS.input" ]; then
    #    exit 0
    #fi
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
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt4/subopt4s/1.tband_plot.py
        exit 0
        ;;
    2) 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/opt4/subopt4s/2.fatband_elements.py
        exit 0
        ;;
    3) 
        echo "投影到轨道"
        exit 0
        ;;
    *) 
        echo -e "\033[35m(*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac
done
}