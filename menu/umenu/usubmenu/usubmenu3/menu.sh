#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
#for i in {1,2,3}
#    do
#        source /data/home/liuhanyu/hyliu/code/pwkit/menu/umenu/usubmenu/usubmenu1/ussubmenu${i}/menu.sh
#    done
source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/ussubmenu1/menu.sh

umenu::usubmenu3() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu3/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        umenu
        ;;
    1)
        usubmenu3::ussubmenu1
        #echo "usubmenu3::ussubmenu1"
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}