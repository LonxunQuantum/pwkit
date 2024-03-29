#!/bin/bash


info_types_lst=([0]="1" [1]="2" [2]="3" [3]="4" [4]="5" [5]="6") 



gsubmenu2::gssubmenu3() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/menu_cn.py
        read -p " ------------>>  
" submenuOpt


    if echo "${info_types_lst[@]}" | grep -w $submenuOpt &>/dev/null;
    then
        ### Step 1. 得到结构文件的`文件名` -- $atom_config_file_name
        echo "
 - 当前目录下共有 $(ls | wc -l) 个文件。搜索当前目录是否含有名为 atom.config 的结构文件..."

        atom_config_file_name="atom.config"  # 默认结构文件名为 atom.config
        while [ ! -f $atom_config_file_name ]
        do
            echo -e "
\033[31m - 未搜索到名为 $atom_config_file_name 的文件，需要手动指定结构文件名...\033[0m"
            read -p " 
 结构文件的名字
 --------------->>
" atom_config_file_name
        done
    fi



    ### Step 2. 根据输入，执行相关的行为
    case $submenuOpt in 
    q|Q)
        exit 0
        ;;
    bb|BB)
        gmenu::gsubmenu2
        ;;
    1)
        # 查看原晶胞的基矢
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt1/opt1_use.py $atom_config_file_name
        exit 0
        ;;
    2)
        # 查看原晶胞的基矢长度
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt2/opt2_use.py $atom_config_file_name
        exit 0
        ;;
    3)
        # 查看原晶胞的基矢间夹角
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt3/opt3_use.py $atom_config_file_name
        exit 0
        ;;
    4)
        # 查看倒易点阵的基矢 (单位: 2pi/埃)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt4/opt4_use.py $atom_config_file_name
        exit 0
        ;;
    5)
        # 查看倒易点阵的基矢长度 (单位: 2pi/埃)
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt5/opt5_use.py $atom_config_file_name
        exit 0
        ;;
    6)
        # 查看晶胞的对称性信息
        $PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu2/gssubmenu3/opt6/opt6_use.py $atom_config_file_name
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}