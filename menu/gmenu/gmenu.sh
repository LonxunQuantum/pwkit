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

    ### Part I: 将 longStr 拆分为多个长度为2的字符串，并执行相应的要求
    #export shiftIdx=1
    #while [ 1 ]
    #do 
    #    tmp=`echo $longStr | cut -c $shiftIdx-$(($shiftIdx+1))`
    #    if [ "$tmp" != "" ]
    #    then
    #        ((shiftIdx++)); ((shiftIdx++));
    #        echo $tmp
    #    else
    #        break
    #    fi
    #done

    ## Part 1. 任务类型 
    $PWKIT_ROOT/menu/gmenu/select_task.py $longStr
    case $longStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    sc|SC)
        echo "SC"
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
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        ;;
    esac
    done
}