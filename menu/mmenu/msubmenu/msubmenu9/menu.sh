#!/bin/bash


# 加载每 msubmenu9 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu9/opt1/menu_opt1.sh


mmenu::msubmenu9() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu9/menu_${glanguage}.py
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
      msubmenu9::menu_opt1
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

