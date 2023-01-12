#!/bin/bash


# 加载 usubmenu 对应的所有opt函数
#for i in {1,2}
#    do  
#        source /data/home/liuhanyu/hyliu/code/pwkit/menu/umenu/usubmenu/ussubmenu${i}/ussubmenu${i}/menu.sh
#    done

source /data/home/liuhanyu/hyliu/code/pwkit/menu/umenu/usubmenu/usubmenu1/ussubmenu1/menu.sh

umenu::usubmenu1() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/menu_cn.py
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
        #echo "usubmenu1::ussubmenu1"
        usubmenu1::ussubmenu1
        exit 0
        ;;
    2)
        usubmenu1::ussubmenu2
        exit 0
        ;;
    3)
        usubmenu1::ussubmenu3
        exit 0
        ;;
    4)
        usubmenu1::ussubmenu4
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}