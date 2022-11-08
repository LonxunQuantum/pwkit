#!/bin/bash


# 加载每 msubmenub 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt4.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt5.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt6.sh

mmenu::msubmenub() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/menu_${glanguage}.py
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
      msubmenub::opt1
      ;;
    2)
      msubmenub::opt2
      ;;
    3)
      msubmenub::opt3
      ;;
    4)
      msubmenub::opt4
      ;;
    5)
      msubmenub::opt5
      ;;
    6)
      msubmenub::opt6
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

