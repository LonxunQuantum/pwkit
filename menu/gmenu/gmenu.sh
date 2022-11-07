#!/bin/bash

# 加载gmenu显示函数
source $PWKIT_ROOT/menu/gmenu/gmenu_cn.sh
source $PWKIT_ROOT/menu/gmenu/gmenu_en.sh

gmenu() {

while [ 1 ]
    do
        gmenu::gmenu_${glanguage}
        read -p " ------------>> " menuOpt
    
    case $menuOpt in
    q|Q)
        exit
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