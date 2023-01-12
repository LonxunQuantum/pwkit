#!/bin/bash


### 加载 usubmenu 对应的所有opt函数
for i in {1,2,3,4,5}
    do
        source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu2/opt${i}/menu_opt${i}_use.sh
    done


usubmenu1::ussubmenu2() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu2/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu::usubmenu1
        ;;
    1)
        ussubmenu2::opt1       
        exit 0
        ;;
    2)
        ussubmenu2::opt2
        exit 0
        ;;
    3)
        ussubmenu2::opt3
        exit 0
        ;;
    4)
        ussubmenu2::opt4
        exit 0
        ;;
    5)
        ussubmenu2::opt5
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}