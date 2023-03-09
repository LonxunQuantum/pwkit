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
#      NS(非自洽计算): 1.KMesh 2.KPATH
tasks_need_kmesh=([0]="SC" [1]="CR" [2]="AR" [3]="DS" [4]="OS" [5]="EP" [6]="MD" [7]="NA" [8]="TD" [9]="TC" [10]="TS")
# 3. 字典: 键 - 选项(数字)； 值 - 格式名(e.g. pwmat, vasp)
declare -A file_format_mark2name
file_format_mark2name=([1]="pwmat" [2]="vasp" [3]="mcsqs" [4]="json" [5]="xsf" [6]="yaml" [7]="cssr" [8]="prismatic")


### Driver code
gmenu::gsubmenu1() {

if [ -f "etot.input" ]; then 
    rm "etot.input"
fi

if [ -f "IN.SOLVENT" ]; then 
    rm "IN.SOLVENT"
fi


#while [ 1 ]
#    do


    while [ 1 ]
    do
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/menu_cn.py
        read -p " ------------>>
" longStr

    # 在输入 `sgpe` 的输入栏中也可以退出
    case $longStr in
    q|Q)
        exit
        ;;
    bb|BB)
        gmenu
        ;;
    esac
    
    # Step 0. 准备工作
    # 1. 提醒用户所设置的东西; 2. 删除 longStr 对特殊设置的重复设置
        #************************************* 任务设置 *************************************
        #    1. 任务类型: 自洽计算
        #    2. 泛函设置: PBE
        #    3. 赝势设置: SG15
        #    4. 特殊设置: 无
        #************************************************************************************
    configStr=`$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/0_output_config.py $longStr`
    #echo $configStr
    mark_AbortOrOutputConfig=`echo $configStr | cut -d';' -f 1`
    if [ "$mark_AbortOrOutputConfig" = "abort_task" ]; then
        echo -e "\033[35m任务类型: (*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
    elif [ "$mark_AbortOrOutputConfig" = "abort_input" ]; then
        echo -e "\033[35m(*_*) Unsupported selection! Try Again... (*_*)\033[0m" 
        echo -e "\033[35m(*_*) Check your input: $longStr! (*_*)\033[0m"
    else # [ "$mark_AbortOrOutputConfig" = "output_config" ]
        # 处理类似于 "自洽计算;PBE;..." 的字符串
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/0_1_process_config_str.py $configStr
        break
    fi
    done


    ### Step 1. 读取结构 -- 如果不存在 atom.config，就生成 atom.config
    echo " - 当前目录下共有 $(ls | wc -l) 个文件。搜索当前目录是否含有 PWmat 格式的结构文件..."

    while [ 1 ]
    do  
    ## Step 1.1. 判断是否存在 atom.config 格式的结构文件
    # atom_config_format_file_name: PWmat 格式的文件的名字
    echo "" # 换行
    atom_config_format_file_name=`$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/1_generate_atom_config.py "judge_atom_config_exist"`
    if [ "$atom_config_format_file_name" != "None" ];then
        echo " - 搜索到 PWmat 格式的结构文件: ${atom_config_format_file_name}
        "
    fi

    if [ ! -f $atom_config_format_file_name ]; then
        echo -e "\033[31m - 未搜索到 PWmat 格式的结构文件，需要手动指定结构文件的格式和文件名...\033[0m
        "
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/1_generate_atom_config.py "structure_convert_warning"
        ## Step 1.2.1. 判断输入的文件格式是否存在
        read -p " 结构文件的格式 
--------------->>
" file_format_mark
        file_format=${file_format_mark2name[$file_format_mark]}
        if ! echo "${file_formats_lst[@]}" | grep -w $file_format &>/dev/null;
        then
            echo -e "\033[35m(*_*) 检查输入的文件格式... (*_*)\033[0m"
            continue
        fi
        ## Step 1.2.2. 判断输入的文件名是否存在
        read -p " 结构文件的名字
--------------->>
" file_name
        if [ ! -f $file_name ];
        then
            echo -e "\033[35m(*_*) 检查输入的文件名是否存在... (*_*)\033[0m"
            continue
        fi

        # 如果由于种种 Exception，导致结构文件的类型转换失败。则 check_structure_file="Check_structure_file"
        check_structure_file=`$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/1_generate_atom_config.py $file_format $file_name`
        
        # 如果结构文件格式转换失败，则输出`异常`
        if [ "$check_structure_file" = "Check_structure_file" ]
        then
            echo -e "\033[35m(*_*) 检查输入的文件内容是否为空... (*_*)\033[0m"
            continue
        fi
        atom_config_format_file_name="atom.config"
        echo " 
 - 已自动生成 atom.config 文件
        "
        break
    else 
        #atom_config_format_file_name="atom.config"
        break   # atom.config 存在的话，直接跳出while循环
    fi
    done


    ### Step 2. 判断任务类型，对于部分任务，应得到 KMesh density
    ## Part I. 任务类型 -- taskStr, 将 longStr[3:] 保存为 restStr
    taskStr=`echo $longStr | cut -c 1-2`
    # taskStr 经处理后，均为大写
    taskStr=`$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/select_task.py $taskStr`

    ### Case 1: 设置 kmesh 的 density
    ## 对于部分任务 (在$tasks_need_kmesh数组中的任务)，输入density (为了后面得到 KMesh)
    if echo "${tasks_need_kmesh[@]}" | grep -w $taskStr &> /dev/null; then 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/generateETOT/warning.py "kmesh_warning"
        if [ "$taskStr" == "ds" -o "$taskStr" == "DS" ] ;then
            echo -e "\033[31m        * 进行DOS计算的时候，density必须与之前计算一致! \033[0m"
            echo -e "+--------------------------------------------------------------------+"
        fi

        read -p " Input Kmesh-Resolved Value (in Units of 2*PI/Angstrom): 
------------>>
" density_in_2pi
    fi

    ### Case 2: 非自洽计算(NS)，需要选择 KMesh or KPATH
    ## 对于部分任务 (在$tasks_need_kmesh数组中的任务)，输入density (为了后面得到 KMesh)
    if [ "$taskStr" == "NS" ]; then 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/2_1_hSP_menu.py
        read -p " 输入 KPoints 的定义方式: 
------------>>
" ns_kpoints_definition_way
        case $ns_kpoints_definition_way in 
        1)
            read -p " Input Kmesh-Resolved Value (in Units of 2*PI/Angstrom): 
------------>>
" density_in_2pi
            ;;
        2)  
            read -p " 输入材料的维度 (2: 二维材料; 3: 三维材料):
------------>>
" dimension_material
            read -p " Input Kmesh-Resolved Value (in Units of 2*PI/Angstrom): 
------------>>
" density_for_kpath
            $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/partOfSteps/2_highSymmetryPoints.py ${atom_config_format_file_name} ${dimension_material} ${density_for_kpath}
            ${PWKIT_ROOT}/menu/scripts/split_kp.x gen.kpt > /dev/null
            ;;
        esac

    fi



    $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu1/generateETOT/etotWritr_main.py $longStr $atom_config_format_file_name $SG15_DIR_PATH $density_in_2pi

    exit 0
#   done
}