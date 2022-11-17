#!/bin/bash

ARR=([0]=item_1 [1]=item_2)
echo ${ARR[@]}

if echo "${ARR[@]}" | grep -w "item_1" &>/dev/null; then
    echo "Found"
fi