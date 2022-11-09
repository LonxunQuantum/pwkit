#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数


mmenu::msubmenud() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/menu_${glanguage}.py
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
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt1.py
      exit 0
      ;;
    2)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt2.py
      exit 0
      ;;
    3)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt3.py
      exit 0
      ;;
    4)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt4.py
      exit 0
      ;;
    5)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt5.py
      exit 0
      ;;
    6)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt6.py
      exit 0
      ;;
    7)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt7.py
      exit 0
      ;;
    8)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt8.py
      exit 0
      ;;
    9)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt9.py
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

