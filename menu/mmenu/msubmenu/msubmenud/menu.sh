#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
for i in `seq 1 9`
  do 
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenud() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/menu_${glanguage}.py
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
      msubmenud::menu_opt1
      exit 0
      ;;
    2)
      msubmenud::menu_opt2
      exit 0
      ;;
    3)
      msubmenud::menu_opt3
      exit 0
      ;;
    4)
      msubmenud::menu_opt4
      exit 0
      ;;
    5)
      msubmenud::menu_opt5
      exit 0
      ;;
    6)
      msubmenud::menu_opt6
      exit 0
      ;;
    7)
      msubmenud::menu_opt7
      exit 0
      ;;
    8)
      msubmenud::menu_opt8
      exit 0
      ;;
    9)
      msubmenud::menu_opt9
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

