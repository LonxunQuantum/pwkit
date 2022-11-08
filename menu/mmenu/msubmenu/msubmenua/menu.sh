#!/bin/bash


# 加载每 msubmenu4 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt4.sh


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
      msubmenua::opt1
      ;;
    2)
      msubmenua::opt2
      ;;
    3)
      msubmenua::opt3
      ;;
    4)
      msubmenua::opt4
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

