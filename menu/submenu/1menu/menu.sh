#!/bin/bash
submenu::1() {
while [ 1 ]
  do
    submenu::1menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::1opt1 ;;
    2)
      submenu::1opt2 ;;
    3)
      submenu::1opt3 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

