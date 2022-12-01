#!/bin/bash


# 加载每 msubmenuh 对应的所有 opt 函数
for i in {1,2,3}
  do 
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenuh() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/menu_${glanguage}.py
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
      msubmenuh::menu_opt1
      exit 0
      ;;
    2)
      msubmenuh::menu_opt2
      exit 0
      ;;
    3)
      msubmenuh::menu_opt3
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

