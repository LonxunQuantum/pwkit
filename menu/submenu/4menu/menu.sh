#!/bin/bash
submenu::4() {
while [ 1 ]
  do
    submenu::4menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::4opt1 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}
