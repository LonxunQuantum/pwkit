#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数


mmenu::msubmenuc() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuc/menu_${glanguage}.py
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
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuc/opt1.py
      exit 0
      ;;
    2)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuc/opt2.py
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

