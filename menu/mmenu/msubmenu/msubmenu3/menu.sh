#!/bin/bash


# 加载每 msubmenu3 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu3/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu3/opt2.sh


mmenu::msubmenu3() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu3/menu_${glanguage}.py
    read -p " ------------>>  
" submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    bb|BB)
      mmenu ;;
    1)
      msubmenu3::opt1 ;;
    2)
      msubmenu3::opt2 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

