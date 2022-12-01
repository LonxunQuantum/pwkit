#!/bin/bash

# 加载每 msubmenu5 对应的所有 opt 函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt1/menu_opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt2/menu_opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt3/menu_opt3.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt4/menu_opt4.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt5/menu_opt5.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt6/menu_opt6.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt7/menu_opt7.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/opt8/menu_opt8.sh


mmenu::msubmenu5() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/menu_${glanguage}.py
    read -p " ------------>> 
" submenuOpt
    case $submenuOpt in
    q|Q)
      # 退出 pwkit 的 conda 环境
      conda deactivate
      exit 0 ;;
    bb|BB)
      mmenu ;;
    1)
      msubmenu5::menu_opt1
      exit 0
      ;;
    2)
      msubmenu5::menu_opt2
      exit 0
      ;;
    3)
      msubmenu5::menu_opt3
      exit 0
      ;;
    4)
      msubmenu5::menu_opt4
      exit 0
      ;;
    5)
      msubmenu5::menu_opt5
      exit 0
      ;;
    6)
      msubmenu5::menu_opt6
      exit 0
      ;;
    7)
      msubmenu5::menu_opt7
      exit 0
      ;;
    8)
      msubmenu5::menu_opt8
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

