#!/bin/bash


# 加载每 msubmenub 对应的所有 opt 函数


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
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt1.py
      exit 0
      ;;
    2)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt2.py
      exit 0
      ;;
    3)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt3.py
      exit 0
      ;;
    4)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt4.py
      exit 0
      ;;
    5)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt5.py
      exit 0
      ;;
    6)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt6.py
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

