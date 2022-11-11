#!/bin/bash


# 加载每 msubmenu4 对应的所有 opt 函数 
for i in {1,2,3,4}
  do
    source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/opt${i}/menu_opt${i}.sh
  done


mmenu::msubmenua() {
while [ 1 ]
  do
    $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/menu_${glanguage}.py
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
      msubmenua::menu_opt1
      exit 0
      ;;
    2)
      msubmenua::menu_opt2
      exit 0
      ;;
    3)
      msubmenua::menu_opt3
      exit 0
      ;;
    4)
      msubmenua::menu_opt4
      exit 0
      ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

