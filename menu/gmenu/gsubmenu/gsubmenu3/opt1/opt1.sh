# 3. 字典: 键 - 选项(数字)； 值 - 格式名(e.g. pwmat, vasp)
declare -A file_format_mark2name
file_format_mark2name=([1]="pwmat" [2]="vasp" [3]="mcsqs" [4]="json" [5]="xsf" [6]="yaml" [7]="cssr" [8]="prismatic")



gsubmenu3::opt1() {

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

### Step 2. 二维材料？三维材料？
read -p " 输入材料的维度 (2: 二维材料; 3: 三维材料):
------------>>
" dimension


### Step 3. 获取每条 KPATH 上的取点密度
read -p " 输入每条KPATH上的取点密度 (单位: 2*PI/Angstrom): 
------------>>
" density_in_2pi


# Step 4. 取出结构的高对称点，输出 HIGHK 和 gen.kpt 文件 （用于 split_kp.x 的输入文件）
$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu3/opt1/1_high_symmetry_points.py ${atom_config_format_file_name} ${dimension} ${density_in_2pi}
$PWKIT_ROOT/menu/scripts/split_kp.x < gen.kpt > /dev/null
# 输出
$PYTHON_PATH $PWKIT_ROOT/menu/gmenu/gsubmenu/gsubmenu3/opt1/2_sum.py $atom_config_format_file_name

}