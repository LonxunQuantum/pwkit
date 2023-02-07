#!/bin/bash


### 加载 usubmenu 对应的所有opt函数: 直接调用 Python 脚本，不需要 source `shell 函数`


usubmenu3::ussubmenu1() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/ussubmenu1/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu::usubmenu3
        ;;
    1)
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/ussubmenu1/opt1/opt1_use.py
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}