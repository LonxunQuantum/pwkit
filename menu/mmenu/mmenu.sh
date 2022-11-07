#!/bin/bash

# 加载menu函数
source $PWKIT_ROOT/menu.sh

# 加载mmenu显示函数
source $PWKIT_ROOT/menu/mmenu/mmenu_cn.sh
source $PWKIT_ROOT/menu/mmenu/mmenu_en.sh

mmenu() {

while [ 1 ]
    do
        mmenu::mmenu_${glanguage}
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