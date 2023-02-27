#!/bin/bash


# 加载每 msubmenui 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenui/opt1/menu_opt1.sh


mmenu::msubmenui() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenui/menu_${glanguage}.py
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
      msubmenui::menu_opt1
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

