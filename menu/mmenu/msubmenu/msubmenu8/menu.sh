#!/bin/bash


# 加载每 msubmenu4 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/opt3.sh


mmenu::msubmenu8() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/menu_${glanguage}.py
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
      msubmenu8::opt1
      ;;
    2)
      msubmenu8::opt2
      ;;
    3)
      msubmenu8::opt3
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

