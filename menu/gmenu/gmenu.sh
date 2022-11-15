#!/bin/bash

# 加载menu函数
#source $PWKIT_ROOT/menu/menu.sh

# 加载gmenu显示函数 -- Python click


gmenu() {

while [ 1 ]
    do
        $PWKIT_ROOT/menu/gmenu/gmenu_cn.py
        read -p " ------------>>
" longStr


    ## Part 1. 任务类型 -- taskStr, 将 longStr[3:] 保存为 restStr
    taskStr=`echo $longStr | cut -c 1-2`
    restStr=`echo $longStr | cut -c 3-`
    # taskStr 经处理后，均为大写
    taskStr=`$PWKIT_ROOT/menu/gmenu/select_task.py $taskStr`

    case $taskStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    sc|SC)
        echo "任务类型: " $taskStr
        ;;
    cr|CR)
        exit 0
        ;;
    ar|AR)
        exit 0
        ;;
    ns|NS)
        exit 0
        ;;
    ds|DS)
        exit 0
        ;;
    os|OS)
        exit 0
        ;;
    ep|EP)
        exit 0
        ;;
    md|MD)
        exit 0
        ;;
    na|NA)
        exit 0
        ;;
    td|TD)
        exit 0
        ;;   
    tc|TC)
        exit 0
        ;;
    ts|TS)
        exit 0
        ;;
    default)
        echo -e "\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        ;;
    *)
        echo -e "\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        ;;
    esac
    done
}