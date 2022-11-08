#!/bin/bash


# 加载每 msubmenuh 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/opt3.sh


mmenu::msubmenuh() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/menu_${glanguage}.py
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
      msubmenuh::opt1
      ;;
    2)
      msubmenuh::opt2
      ;;
    3)
      msubmenuh::opt3
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

