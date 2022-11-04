#!/bin/bash
submenu::3() {
while [ 1 ]
  do
    submenu::3menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::3opt1 ;;
    2)
      submenu::3opt2 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

