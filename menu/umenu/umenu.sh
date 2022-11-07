#!/bin/bash

# 加载menu函数
source $PWKIT_ROOT/menu.sh

# 加载umenu显示函数
source $PWKIT_ROOT/menu/umenu/umenu_cn.sh
source $PWKIT_ROOT/menu/umenu/umenu_en.sh

umenu() {

while [ 1 ]
    do
        umenu::umenu_${glanguage}
        read -p " ------------>> " menuOpt
    
    case $menuOpt in
    q|Q)
        exit
        ;;
    b|B)
        menu
        ;;
    1)
        exit    
        ;;
    2) 
        exit
        ;;

    esac
    done
}