#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
for i in {1,2,3,4}
  do 
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenuf() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/menu_${glanguage}.py
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
      msubmenuf::menu_opt1
      exit 0
      ;;
    2)
      msubmenuf::menu_opt2
      exit 0
      ;;
    3)
      msubmenuf::menu_opt3
      exit 0
      ;;
    4)
      msubmenuf::menu_opt4
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

