#!/bin/bash


# 加载1msubmenu显示函数
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu1/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu2/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu3/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu4/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu5/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu6/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu7/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu8/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenu9/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenua/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenub/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuc/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenud/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenue/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuf/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenug/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuh/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenui/menu.sh
source $PWKIT_ROOT/menu/mmenu/msubmenu/msubmenuj/menu.sh


mmenu() {

while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/mmenu/mmenu_cn.py
        read -p " ------------>>
" menuOpt
    
    case $menuOpt in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    1)
        mmenu::msubmenu1    # 结构搜索
        ;;
    2) 
        mmenu::msubmenu2    # 无序结构
        ;;
    3)
        mmenu::msubmenu3    # 分子动力学数据处理
        ;;
    4) 
        mmenu::msubmenu4    # CIF 文件转换与结构处理
        ;;
    5) 
        mmenu::msubmenu5    # 电子结构
        ;;
    6) 
        mmenu::msubmenu6    # 声子计算
        ;;
    7) 
        mmenu::msubmenu7    # 光学性质
        ;;
    8)
        mmenu::msubmenu8    # 磁学性质
        ;;
    9)
        mmenu::msubmenu9    # 力学性质
        ;; 
    a)
        mmenu::msubmenua    # 极化性质
        ;; 
    b)
        mmenu::msubmenub    # 缺陷性质
        ;; 
    c)
        mmenu::msubmenuc    # 电化学性质
        ;; 
    d)
        mmenu::msubmenud    # 输运性质
        ;; 
    e)
        mmenu::msubmenue    # 超快动力学
        ;;      
    f)
        mmenu::msubmenuf    # Beyond DFT
        ;;      
    g)
        mmenu::msubmenug    # 电子束辐照分解
        ;; 
    h)
        mmenu::msubmenuh    # 大体系计算
        ;; 
    i)
        mmenu::msubmenui    # 机器学习力场
        ;; 
    j)
        mmenu::msubmenuj    # 其他
        ;; 
    *)
      echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}