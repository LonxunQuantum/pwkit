#!/bin/bash

# 加载menu函数
#source $PWKIT_ROOT/menu/menu.sh

# 加载gmenu显示函数 -- Python click


gmenu() {

if [ -f "etot.input" ]; then 
    rm "etot.input"
fi


while [ 1 ]
    do
        $PWKIT_ROOT/menu/gmenu/gmenu_cn.py
        read -p " ------------>>
" longStr
        read -p " Input Kmesh-Resolved Value (in Units of 2*PI/Angstrom): 
------------>>
" density_in_2pi


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
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    cr|CR)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ar|AR)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ns|NS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ds|DS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    os|OS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ep|EP)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    md|MD)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    na|NA)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    td|TD)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;   
    tc|TC)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ts|TS)
        echo "任务类型: " $taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
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
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    91)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    ps|PS)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    ld|LD)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    h6|H6)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    h3|H3)
        echo "任务类型: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    p0|P0)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    b3|B3)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    tp|TP)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    sc|SC)
        echo "泛函设置: " $functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;   
    default)
        functionalStr="PE"
        echo "泛函设置: " $functionalStr
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        #restStr=$restStr
        ;;
    *)
        echo -e "\033[35m泛函设置: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac

    ### 写入 ACCURACY 设置
    $PWKIT_ROOT/menu/gmenu/generateETOT/3_write_accuracy.py
    ### 写入 #电子自洽设置
    $PWKIT_ROOT/menu/gmenu/generateETOT/4_write_scf.py $density_in_2pi


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
        echo "赝势设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pd|PD)
        echo "赝势设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    fh|FH)
        echo "赝势设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pw|PW)
        echo "赝势设置: " $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    default)        
        pseudoStr="SG"
        echo "泛函设置: " $pseudoStr
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
        $PWKIT_ROOT/menu/gmenu/generateETOT/5_write_specific.py $specificStr
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


    # 当 restStr 等于 ""，写入输入输出设置后，退出程序
    if [ "$restStr" = "$endMark" ]
    then
        ### 写入 `输入输出设置` 到 `etot.input`
        $PWKIT_ROOT/menu/gmenu/generateETOT/6_write_input_output.py $pseudoStr
        exit 0
    fi

    done
}