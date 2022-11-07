#!/bin/bash


# 加载中/英显示菜单的函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/menu_cn.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/menu_en.sh

# 加载每xmsubmenu对应的所有opt函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/1msubmenu/opt3.sh

mmenu::1() {
while [ 1 ]
  do
    1msubmenu::1menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      mmenu ;;
    1)
      1msubmenu::1opt1 ;;
    2)
      1msubmenu::1opt2 ;;
    3)
      1msubmenu::1opt3 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

