#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/opt3.sh


mmenu::msubmenug() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/menu_${glanguage}.py
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
      msubmenug::opt1
      ;;
    2)
      msubmenug::opt2
      ;;
    3)
      msubmenug::opt3
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

