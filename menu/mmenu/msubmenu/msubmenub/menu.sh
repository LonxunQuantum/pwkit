#!/bin/bash


# 加载每 msubmenub 对应的所有 opt 函数
for i in {1,2,3,4,5,6}
  do 
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenub() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/menu_${glanguage}.py
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
      msubmenub::menu_opt1
      exit 0
      ;;
    2)
      msubmenub::menu_opt2
      exit 0
      ;;
    3)
      msubmenub::menu_opt3
      exit 0
      ;;
    4)
      msubmenub::menu_opt4
      exit 0
      ;;
    5)
      msubmenub::menu_opt5
      exit 0
      ;;
    6)
      msubmenub::menu_opt6
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

