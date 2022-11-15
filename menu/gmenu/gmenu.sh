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


    ### Part I. 任务类型 -- taskStr, 将 longStr[3:] 保存为 restStr
    taskStr=`echo $longStr | cut -c 1-2`
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
        restStr=`echo $longStr | cut -c 3-`
        ;;
    cr|CR)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    ar|AR)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    ns|NS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    ds|DS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    os|OS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    ep|EP)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    md|MD)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    na|NA)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    td|TD)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;   
    tc|TC)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    ts|TS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        ;;
    default)
        echo -e "\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    *)
        echo -e "\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac


    ### Part II. 泛函设置 -- functionalStr, 将 restStr[3:] 保存为 restStr
    functionalStr=`echo $restStr | cut -c 1-2`
    # functionalStr 经处理后，均为大写
    functionalStr=`$PWKIT_ROOT/menu/gmenu/select_functional.py $functionalStr`

    case $functionalStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    pe|PE)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    91)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    ps|PS)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    ld|LD)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    h6|H6)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    h3|H3)
        echo "任务类型: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    p0|P0)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    b3|B3)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    tp|TP)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    sc|SC)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        ;;   
    default)
        functionalStr="默认"
        echo "泛函设置: " $functionalStr
        #restStr=$restStr
        ;;
    *)
        echo -e "\033[35m泛函设置: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac



    ### Part III. 赝势设置 -- pseudoStr, 将 restStr[3:] 保存为 restStr
    pseudoStr=`echo $restStr | cut -c 1-2`
    # functionalStr 经处理后，均为大写
    pseudoStr=`$PWKIT_ROOT/menu/gmenu/select_pseudo.py $pseudoStr`

    case $pseudoStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    sg|SG)
        echo "泛函设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pd|PD)
        echo "泛函设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    fh|FH)
        echo "泛函设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pw|PW)
        echo "泛函设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    default)
        pseudoStr="默认"
        echo "泛函设置: " $pseudoStr
        #restStr=$restStr
        ;;
    *)
        echo -e "\033[35m赝势设置: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac


    ### Part IV. 特殊设置 -- specificStr, 将 restStr[3:] 保存为 restStr
    endMark=`echo "123" | cut -c 4`
    if [ "$restStr" = "$endMark" ]
        then
        echo "特殊设置: " "None"
        exit 0
    fi

    until [ "$restStr" = "$endMark" ]
    do 
    specificStr=`echo $restStr | cut -c 1-2`
    # functionalStr 经处理后，均为大写
    specificStr=`$PWKIT_ROOT/menu/gmenu/select_specific.py $specificStr`
    case $specificStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    sp|SP)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    so|SO)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    sn|SN)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    cs|CS)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pu|PU)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    d3|D3)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    ff|FF)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    se|SE)
        echo "特殊设置: " $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    default)
        pseudoStr="默认"
        echo "特殊设置: 无" 
        #restStr=$restStr
        ;;
    *)
        echo -e "\033[35m(*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        echo -e "\033[35m(*_*) Check your input: $longStr! (*_*)\033[0m"
        break
        ;;
    esac
    done

    # 当 restStr 等于 ""，退出程序
    if [ "$restStr" = "$endMark" ]
    then
        exit 0
    fi

    done
}