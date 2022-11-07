#!/bin/bash
# menu
source $PWKIT_ROOT/menu/menu_cn.sh
source $PWKIT_ROOT/menu/menu_en.sh

# gmenu package函数的载入
source $PWKIT_ROOT/menu/gmenu/gmenu.sh

# mmenu package函数的载入
source $PWKIT_ROOT/menu/mmenu/mmenu.sh

# umenu package函数的载入
source $PWKIT_ROOT/menu/umenu/umenu.sh


menu() {
    while [ 1 ]
        do
            menu::menu_${glanguage} | fold -w 70 -s
            read -p " ------------>> " menuOpt
        
            case $menuOpt in 
            q|Q)
                exit 0
                ;;
            g|G)
                gmenu
                ;;
            m|M)
                mmenu
                ;;
            u|U)
                umenu
                ;;
            esac
        done
}