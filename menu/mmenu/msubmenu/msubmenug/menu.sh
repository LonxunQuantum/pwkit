#!/bin/bash


# 加载每 msubmenuc 对应的所有 opt 函数
for i in {1,2,3}
  do 
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenug() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/menu_${glanguage}.py
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
      msubmenug::menu_opt1
      exit 0
      ;;
    2)
      msubmenug::menu_opt2
      exit 0
      ;;
    3)
      msubmenug::menu_opt3
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

