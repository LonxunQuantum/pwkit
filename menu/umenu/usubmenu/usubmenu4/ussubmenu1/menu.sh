#!/bin/bash


### 加载 usubmenu 对应的所有opt函数
#for i in {1,2,3,4,5,6}
#    do
#        source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu1/opt${i}/menu_opt${i}_use.sh
#    done
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu4/ussubmenu1/opt1/menu_opt1_use.sh


usubmenu4::ussubmenu1() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu4/ussubmenu1/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu::usubmenu4
        ;;
    1)
        ussubmenu4::opt1
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}