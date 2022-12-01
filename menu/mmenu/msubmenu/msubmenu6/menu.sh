#!/bin/bash

# 加载每 msubmenu5 对应的所有 opt 函数 
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/opt1/menu_opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/opt2/menu_opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/opt3/menu_opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/opt4/menu_opt4.sh


mmenu::msubmenu6() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/menu_${glanguage}.py
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
      msubmenu6::menu_opt1
      exit 0
      ;;
    2)
      msubmenu6::menu_opt2
      exit 0
      ;;
    3)
      msubmenu6::menu_opt3
      exit 0
      ;;
    4)
      msubmenu6::menu_opt4
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

