#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt4.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt5.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt6.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt7.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt8.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt9.sh


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
      msubmenud::opt1
      ;;
    2)
      msubmenud::opt2
      ;;
    3)
      msubmenud::opt3
      ;;
    4)
      msubmenud::opt4
      ;;
    5)
      msubmenud::opt5
      ;;
    6)
      msubmenud::opt6
      ;;
    7)
      msubmenud::opt7
      ;;
    8)
      msubmenud::opt8
      ;;
    9)
      msubmenud::opt9
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

