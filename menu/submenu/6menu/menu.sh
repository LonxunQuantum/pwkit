#!/bin/bash
submenu::6() {
while [ 1 ]
  do
    submenu::6menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::6opt1 ;;
    2)
      submenu::6opt2 ;;
    3)
      submenu::6opt3 ;;
    4)
      submenu::6opt4 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

