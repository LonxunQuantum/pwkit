#!/bin/bash


mmenu::msubmenuj() {
while [ 1 ]
  do
    $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuj/menu_${glanguage}.py
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
    #1)
    #  msubmenui::opt1
    #  ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

