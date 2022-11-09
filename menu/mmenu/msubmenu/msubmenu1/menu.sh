#!/bin/bash


# 用于返回：加载中/英显示菜单的函数 -- Python click
#source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu_cn.sh
#source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu_en.sh

# 加载每 msubmenu对应的所有opt函数 -- Python click -- opt1.py, opt2.py, ...

mmenu::msubmenu1() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu_${glanguage}.py
    read -p " ------------>>  
" submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0
      ;;
    bb|BB)
      mmenu
      ;;
    1)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt1.py
      exit 0
      ;;
    2)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt2.py
      exit 0
      ;;
    3)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt3.py
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}