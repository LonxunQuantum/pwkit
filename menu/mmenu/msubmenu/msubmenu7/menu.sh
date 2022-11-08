#!/bin/bash

# 加载每 msubmenu4 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt4.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt5.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt6.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt7.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt8.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opt9.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/opta.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/optb.sh

mmenu::msubmenu7() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/menu_${glanguage}.py
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    bb|BB)
      mmenu ;;
    1)
      msubmenu7::opt1 ;;
    2)
      msubmenu7::opt2 ;;
    3)
      msubmenu7::opt3 ;;
    4)
      msubmenu7::opt4 ;;
    5)
      msubmenu7::opt5 ;;
    6)
      msubmenu7::opt6 ;;
    7)
      msubmenu7::opt7 ;;
    8)
      msubmenu7::opt8 ;;
    9)
      msubmenu7::opt9 ;;
    a)
      msubmenu7::opta ;;
    b)
      msubmenu7::optb ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

