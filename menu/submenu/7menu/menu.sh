#!/bin/bash
submenu::7() {
while [ 1 ]
  do
    submenu::7menu_${glanguage}
    read -p " ------------>>  " submenuOpt
    case $submenuOpt in
    q|Q)
      exit 0 ;;
    bb)
      menu ;;
    1)
      submenu::7opt1 ;;
    2)
      submenu::7opt2 ;;
    3)
      submenu::7opt3 ;;
    4)
      submenu::7opt4 ;;
    5)
      submenu::7opt5 ;;
    6)
      submenu::7opt6 ;;
    7)
      submenu::7opt7 ;;
    8)
      submenu::7opt8 ;;
    9)
      submenu::7opt9 ;;
    a)
      submenu::7opta ;;
    b)
      submenu::7optb ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

