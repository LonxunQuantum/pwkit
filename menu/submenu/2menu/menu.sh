#!/bin/bash
submenu::2() {
while [ 1 ]
  do
    submenu::2menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::2opt1 ;;
    2)
      submenu::2opt2 ;;
    3)
      submenu::2opt3 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

