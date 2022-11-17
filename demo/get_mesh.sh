function get_kmesh(){
    filename=$1
    density=$2
    if [ -z "$density" ]
    then
        density=0.03
    fi
    b_length=(`atominfo.x ${filename} | awk 'END {print $1,$2,$3}'`)
    kmesh=(`echo ${b_length[@]} ${density}|awk '{printf("%4u%4u%4u",$1/$4,$2/$4,$3/$4)}'`)
cat >> etot.input << EOF
MP_N123 = ${kmesh[@]} 0 0 0 0       # 0(with symmetry), 2(without symmetry)
EOF
}


get_kmesh
