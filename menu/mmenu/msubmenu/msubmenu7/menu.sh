#!/bin/bash

# 加载每 msubmenu4 对应的所有 opt 函数
for i in {1,2,3,4,5,6,7,8,9,a,b}
  do
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenu7() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/menu_${glanguage}.py
    read -p " ------------>>
" submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    bb|BB)
      mmenu ;;
    1)
      msubmenu7::menu_opt1
      exit 0
      ;;
    2)
      msubmenu7::menu_opt2
      exit 0
      ;;
    3)
      msubmenu7::menu_opt3
      exit 0
      ;;
    4)
      msubmenu7::menu_opt4
      exit 0
      ;;
    5)
      msubmenu7::menu_opt5
      exit 0
      ;;
    6)
      msubmenu7::menu_opt6
      exit 0
      ;;
    7)
      msubmenu7::menu_opt7
      exit 0
      ;;
    8)
      msubmenu7::menu_opt8
      exit 0
      ;;
    9)
      msubmenu7::menu_opt9
      exit 0
      ;;
    a)
      msubmenu7::menu_opta
      exit 0
      ;;
    b)
      msubmenu7::menu_optb
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

