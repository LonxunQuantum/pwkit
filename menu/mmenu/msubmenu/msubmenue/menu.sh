#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenue/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenue/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenue/opt3.sh


mmenu::msubmenue() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenue/menu_${glanguage}.py
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
      msubmenue::opt1
      ;;
    2)
      msubmenue::opt2
      ;;
    3)
      msubmenue::opt3
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

