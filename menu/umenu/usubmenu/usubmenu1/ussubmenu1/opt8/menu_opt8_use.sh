#!/bin/bash


# 为了防止不同的 usubmenu 中的 optx 相互覆盖，我们采用以下的命名方式：
#   1. usubmenu1 -> ussubmenu1::opt1
#   2. usubmenu2 -> 1ussubmenu1::opt1
#   3. usubmenu3 -> 11ussubmenu1::opt1
#   4. usubnemu4 -> 111ussubmenu1::opt1
ussubmenu1::opt8() {

    $PYTHON_PATH $PWKIT_ROOT/menu/umenu/usubmenu/usubmenu1/ussubmenu1/opt8/opt8_use.py

}