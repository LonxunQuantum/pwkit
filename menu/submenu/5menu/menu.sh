#!/bin/bash
submenu::5() {
while [ 1 ]
  do
    submenu::5menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    b|B)
      menu ;;
    1)
      submenu::5opt1 ;;
    2)
      submenu::5opt2 ;;
    3)
      submenu::5opt3 ;;
    4)
      submenu::5opt4 ;;
    5)
      submenu::5opt5 ;;
    6)
      submenu::5opt6 ;;
    7)
      submenu::5opt7 ;;
    8)
      submenu::5opt8 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

