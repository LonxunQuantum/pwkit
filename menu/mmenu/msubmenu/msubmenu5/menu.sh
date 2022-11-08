#!/bin/bash

# 加载每 msubmenu4 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt4.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt5.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt6.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt7.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt8.sh


mmenu::msubmenu5() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/menu_${glanguage}.py
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    bb|BB)
      mmenu ;;
    1)
      msubmenu5::opt1 ;;
    2)
      msubmenu5::opt2 ;;
    3)
      msubmenu5::opt3 ;;
    4)
      msubmenu5::opt4 ;;
    5)
      msubmenu5::opt5 ;;
    6)
      msubmenu5::opt6 ;;
    7)
      msubmenu5::opt7 ;;
    8)
      msubmenu5::opt8 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

