#!/bin/bash
# menu
source $PWKIT_ROOT/menu/menu_cn.sh
source $PWKIT_ROOT/menu/menu_en.sh

# submenu => 1menu
source $PWKIT_ROOT/menu/submenu/1menu/menu.sh
source $PWKIT_ROOT/menu/submenu/1menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/1menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/1menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/1menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/1menu/opt3.sh

# submenu => 2menu
source $PWKIT_ROOT/menu/submenu/2menu/menu.sh
source $PWKIT_ROOT/menu/submenu/2menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/2menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/2menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/2menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/2menu/opt3.sh

# submenu => 3menu
source $PWKIT_ROOT/menu/submenu/3menu/menu.sh
source $PWKIT_ROOT/menu/submenu/3menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/3menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/3menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/3menu/opt2.sh

# submenu => 4menu
source $PWKIT_ROOT/menu/submenu/4menu/menu.sh
source $PWKIT_ROOT/menu/submenu/4menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/4menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/4menu/opt1.sh

# submenu => 5menu
source $PWKIT_ROOT/menu/submenu/5menu/menu.sh
source $PWKIT_ROOT/menu/submenu/5menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/5menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt3.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt4.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt5.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt6.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt7.sh
source $PWKIT_ROOT/menu/submenu/5menu/opt8.sh

# submenu => 6menu
source $PWKIT_ROOT/menu/submenu/6menu/menu.sh
source $PWKIT_ROOT/menu/submenu/6menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/6menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/6menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/6menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/6menu/opt3.sh
source $PWKIT_ROOT/menu/submenu/6menu/opt4.sh

# submenu => 7menu  光学性质
source $PWKIT_ROOT/menu/submenu/7menu/menu.sh
source $PWKIT_ROOT/menu/submenu/7menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/7menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt3.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt4.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt5.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt6.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt7.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt8.sh
source $PWKIT_ROOT/menu/submenu/7menu/opt9.sh
source $PWKIT_ROOT/menu/submenu/7menu/opta.sh
source $PWKIT_ROOT/menu/submenu/7menu/optb.sh

# submenu => 8menu
source $PWKIT_ROOT/menu/submenu/8menu/menu.sh
source $PWKIT_ROOT/menu/submenu/8menu/menu_cn.sh
source $PWKIT_ROOT/menu/submenu/8menu/menu_en.sh
source $PWKIT_ROOT/menu/submenu/8menu/opt1.sh
source $PWKIT_ROOT/menu/submenu/8menu/opt2.sh
source $PWKIT_ROOT/menu/submenu/8menu/opt3.sh

menu() {
  # echo $PWKIT_ROOT
while [ 1 ]
  do
    menu::menu_${glanguage}
    read -p " ------------>>  " menuOpt

    # echo -en "\n\n\t\t\tHit any key to continue"
    # read -n 1 line
    case $menuOpt in
    q|Q)
      exit 0 ;;
    1)
      submenu::1 ;;       # 结构搜索
    2)
      submenu::2 ;;       # 无序结构
    3)
      submenu::3 ;;       # 分子动力学数据处理
    4)
      submenu::4 ;;       # CIF 文件转换与结构处理
    5)
      submenu::5 ;;       # 电子结构
    6)
      submenu::6 ;;       # 声子计算
    7)
      submenu::7 ;;       # 光学性质
    8)
      submenu::8 ;;       # 磁学性质
    9)
      submenu::9 ;;       # 力学性质
    a)
      submenu::a ;;       # 极化性质
    b)
      submenu::b ;;       # 缺陷性质
    c)
      submenu::c ;;       # 其它

    ### 直接进入子菜单 ###
    11)
      submenu::1opt1 ;;
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
  done
}

