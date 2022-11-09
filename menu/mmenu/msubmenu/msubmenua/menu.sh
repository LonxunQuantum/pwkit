#!/bin/bash


# 加载每 msubmenu4 对应的所有 opt 函数 -- Python Click: opt1.py, ...


mmenu::msubmenua() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/menu_${glanguage}.py
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
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt1.py
      exit 0
      ;;
    2)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt2.py
      exit 0
      ;;
    3)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt3.py
      exit 0
      ;;
    4)
      $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt4.py
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

