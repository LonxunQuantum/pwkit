#!/bin/bash

# 加载menu函数
#source $PWKIT_ROOT/menu/menu.sh

### 生成 etot.input 步骤
# Step 0. 预处理输入字符串: 1. 提醒用户所设置的东西; 2. 删除 longStr 对特殊设置的重复设置
# Step 1. 读取结构: 各种格式的结构文件
# Step 2. 判断任务类型, 部分任务需要输入 kmesh density
# Step 3. 部分任务读取 KMesh
# Step 4. 泛函设置、赝势设置
# Step 5. 特殊设置


### Key global parameters
# 1.pflow 可以支持的结构文件类型
file_formats_lst=([0]="pwmat" [1]="vasp" [2]="mcsqs" [3]="json" [4]="xsf" [5]="yaml" [6]="cssr" [7]="prismatic")
# 2. 需要输入 KMesh 的任务类型
tasks_need_kmesh=([0]="SC" [1]="CR" [2]="AR" [3]="NS" [4]="DS" [5]="OS" [6]="EP" [7]="MD" [8]="NA" [9]="TD" [10]="TC" [11]="TS")
# 3. 字典: 键 - 选项(数字)； 值 - 格式名(e.g. pwmat, vasp)
declare -A file_format_mark2name
file_format_mark2name=([1]="pwmat" [2]="vasp" [3]="mcsqs" [4]="json" [5]="xsf" [6]="yaml" [7]="cssr" [8]="prismatic")

### Driver code
gmenu() {

if [ -f "etot.input" ]; then 
    rm "etot.input"
fi


while [ 1 ]
    do
        $PWKIT_ROOT/menu/gmenu/gmenu_cn.py
        read -p " ------------>>
" longStr

    # 在输入 `sgpe` 的输入栏中也可以退出
    case $longStr in
    q|Q)
        exit
        ;;
    bb|BB)
        menu
        ;;
    esac
    
    
    # Step 0. 准备工作
    # 1. 提醒用户所设置的东西; 2. 删除 longStr 对特殊设置的重复设置
    `$PWKIT_ROOT/menu/gmenu/partOfSteps/0_preprocess_input_str.py $longStr`
    #echo "TaskName: $tmp"


    ### Step 1. 读取结构 -- 如果不存在 atom.config，就生成 atom.config
    while [ 1 ]
    do  
    if [ ! -f "atom.config" ]; then
        $PWKIT_ROOT/menu/gmenu/partOfSteps/1_generate_atom_config.py "structure_convert_warning"
        
        read -p " 结构文件的格式 
--------------->>
" file_format_mark
        file_format=${file_format_mark2name[$file_format_mark]}
        if ! echo "${file_formats_lst[@]}" | grep -w $file_format &>/dev/null;
        then
            echo -e "\033[35m(*_*) 检查输入的文件格式... (*_*)\033[0m"
            continue
        fi
        read -p " 结构文件的名字
--------------->>
" file_name
        if [ ! -e $file_name ];
        then
            echo "\033[35m(*_*) 检查输入的文件名是否存在... \(*_*)\033[0m"
            continue
        fi
        $PWKIT_ROOT/menu/gmenu/partOfSteps/1_generate_atom_config.py $file_format $file_name
        break
    else 
        break   # atom.config 存在的话，直接跳出while循环
    fi
    done


    ### Step 2. 判断任务类型，对于部分任务，应得到 KMesh density
    ## Part I. 任务类型 -- taskStr, 将 longStr[3:] 保存为 restStr
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
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    cr|CR)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ar|AR)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ns|NS)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ds|DS)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    os|OS)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ep|EP)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    md|MD)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    na|NA)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    td|TD)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;   
    tc|TC)
        echo "Part I. 任务类型设置成功..." #$taskStr
        restStr=`echo $longStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/1_write_task.py $taskStr
        ;;
    ts|TS)
        echo "Part I. 任务类型设置成功..." #$taskStr
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

    ## 对于部分任务 (在$tasks_need_kmesh数组中的任务)，输入density (为了后面得到 KMesh)
    if echo "$tasks_need_kmesh[@]" | grep -w $taskStr &> /dev/null; then 
        $PWKIT_ROOT/menu/gmenu/generateETOT/warning.py "kmesh_warning"
        read -p " Input Kmesh-Resolved Value (in Units of 2*PI/Angstrom): 
------------>>
" density_in_2pi
    fi



    ## Part II. 泛函设置 -- functionalStr, 将 restStr[3:] 保存为 restStr
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
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    91)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    ps|PS)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    ld|LD)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    h6|H6)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    h3|H3)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    p0|P0)
        echo "Part II. 泛函类型设置成功..." #$functionalStrr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    b3|B3)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    tp|TP)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;
    sc|SC)
        echo "Part II. 泛函类型设置成功..." #$functionalStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/2_write_functional.py $functionalStr
        ;;   
    default)
        functionalStr="PE"
        echo "Part II. 泛函类型设置成功..." #$functionalStr
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


    ## Part III. 赝势设置 -- pseudoStr, 将 restStr[3:] 保存为 restStr
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
        echo "Part III. 赝势类型设置成功..." # $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pd|PD)
        echo "Part III. 赝势类型设置成功..." # $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    fh|FH)
        echo "Part III. 赝势类型设置成功..." # $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pw|PW)
        echo "Part III. 赝势类型设置成功..." # $pseudoStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    default)        
        pseudoStr="SG"
        echo "Part III. 赝势类型设置成功..." # $pseudoStr
        ;;
    *)
        echo -e "\033[35m赝势设置: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        continue
        ;;
    esac


    ## Part IV. 特殊设置 -- specificStr, 将 restStr[3:] 保存为 restStr
    endMark=`echo "123" | cut -c 4`
    if [ "$restStr" = "$endMark" ]
        then
        echo "Part IV. 未输入特殊设置"
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
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        $PWKIT_ROOT/menu/gmenu/generateETOT/5_write_specific.py $specificStr
        ;;
    so|SO)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    sn|SN)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    cs|CS)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    pu|PU)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    d3|D3)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    ff|FF)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    se|SE)
        echo "Part IV. 特殊设置成功..." # $specificStr
        restStr=`echo $restStr | cut -c 3-`
        ;;
    default)
        pseudoStr="默认"
        echo "Part IV. 未输入特殊设置..." # $specificStr
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