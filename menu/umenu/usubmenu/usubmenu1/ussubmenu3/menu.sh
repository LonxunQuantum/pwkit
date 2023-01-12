#!/bin/bash


### 加载 usubmenu 对应的所有opt函数
#for i in {1,2,3,4}
#    do
#        source $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu2/opt${i}/menu_opt${i}_use.sh
#    done


usubmenu1::ussubmenu3() {
while [ 1 ]
    do 
        $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu3/menu_cn.py
        read -p " ------------>>  
" submenuOpt

    case $submenuOpt in 
    q|Q)
        # 退出 pwkit 的 conda 环境
        conda deactivate
        exit 0
        ;;
    bb|BB)
        #umenu::usubmenu1   
        ;;
    1)
        #ussubmenu2::opt1   # 查看原晶胞的基矢
        exit 0
        ;;
    2)
        #ussubmenu2::opt2   # 查看倒易点阵的基矢
        exit 0
        ;;
    3)
        #ussubmenu2::opt3   # 查看原晶胞的基矢长度
        exit 0
        ;;
    4)
        #ussubmenu2::opt4   # 查看原晶胞的基矢间夹角
        exit 0
        ;;
    *)
        echo -e "\033[35m (*_*) Unsupported selection! Try Again... (*_*)\033[0m" ;;
    esac
    done
}