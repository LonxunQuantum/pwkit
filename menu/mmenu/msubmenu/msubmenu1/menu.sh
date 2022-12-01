#!/bin/bash


# 用于返回：加载中/英显示菜单的函数 -- Python click
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt1/menu_opt1.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt2/menu_opt2.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/opt3/menu_opt3.sh


# 加载每 msubmenu对应的所有opt函数 -- Python click -- opt1.py, opt2.py, ...

mmenu::msubmenu1() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu_${glanguage}.py
    read -p " ------------>>  
" submenuOpt
    case $submenuOpt in
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
      exit 0
      ;;
    bb|BB)
      mmenu
      ;;
    1)
      msubmenu1::menu_opt1
      exit 0
      ;;
    2)
      msubmenu1::menu_opt2
      exit 0
      ;;
    3)
      msubmenu1::menu_opt3
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}



mmenu::return_msubmenu1() {
  mmenu::msubmenu1
}