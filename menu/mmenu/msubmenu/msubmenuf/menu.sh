#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/opt4.sh


mmenu::msubmenuf() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/menu_${glanguage}.py
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
      msubmenuf::opt1
      ;;
    2)
      msubmenuf::opt2
      ;;
    3)
      msubmenuf::opt3
      ;;
    4)
      msubmenuf::opt4
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

