#!/bin/bash

#until [ $# -eq 0 ]
#    do
#        echo "第一个参数为: $1 参数个数为: $#"
#        shift
#    done

#echo "输入的参数：$@"
#for key in $*
# do
#    echo $key;
#done

read -p " ------------>>
" longStr
shiftIdx=1
/data/home/liuhanyu/hyliu/code/pwkit/menu/gmenu/select_task.py $longStr
while [ 1 ]
do  
    tmp=`echo $longStr | cut -c $shiftIdx-$(($shiftIdx+1))`   # tmp 为长度等于2的字符串
    if [ "$tmp" != "" ]  
    then  
        ((shiftIdx++));((shiftIdx++));    # 每次移动两个字符
        echo $tmp
    else  
        break  
    fi  
done  