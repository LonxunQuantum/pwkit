#!/bin/bash

# 展现 menu 选项的函数：menu_cn.py, menu_en.py

# gmenu package函数的载入
source $PWKIT_ROOT/menu/gmenu/gmenu.sh

# mmenu package函数的载入
source $PWKIT_ROOT/menu/mmenu/mmenu.sh

# umenu package函数的载入
source $PWKIT_ROOT/menu/umenu/umenu.sh


menu() {
    while [ 1 ]
        do
            $PYTHON_PATH $PWKIT_ROOT/menu/menu_cn.py     # 显示菜单
            read -p " ------------>> 
" menuOpt 
        
            case $menuOpt in 
            q|Q)
                exit 0
                ;;
            g|G)
                gmenu   # 进入 Generator 部分
                ;;
            m|M)
                mmenu   # 进入 Module 部分
                ;;
            u|U)
                umenu   # 进入 Utility 部分
                ;;
            *)
                echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
            esac
        done
}